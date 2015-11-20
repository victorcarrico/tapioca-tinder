# coding: utf-8

import json
import requests

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from .resource_mapping import RESOURCE_MAPPING


class TinderClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.gotinder.com/'
    resource_mapping = RESOURCE_MAPPING
    headers = {
        'app_version': '3',
        'platform': 'ios',
        'Content-Type': 'application/json'
    }

    def _get_tinder_token(self, fb_auth_token, fb_user_id):
        response = requests.post(
            '{}auth'.format(self.api_root),
            headers=self.headers,
            data=json.dumps({'facebook_token': fb_auth_token,
                             'facebook_id': fb_user_id})
        )
        try:
            token = response.json()['token']
        except KeyError as err:
            err.args += ('An authentication error may have occured.', )
            raise

        return token

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(TinderClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)
        self.headers['X-Auth-Token'] = self._get_tinder_token(
            api_params.get('fb_auth_token', ''),
            api_params.get('fb_user_id', ''))
        params['headers'] = self.headers

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Tinder = generate_wrapper_from_adapter(TinderClientAdapter)
