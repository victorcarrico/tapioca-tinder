# coding: utf-8

RESOURCE_MAPPING = {
    'profile': {
        'resource': 'profile',
        'docs': 'https://gist.github.com/rtt/10403467#updating-your-profile',
        'methods': ['GET', 'POST'],
    },
    'report_user': {
        'resource': 'report/{id}',
        'docs': 'https://gist.github.com/rtt/10403467#reporting-a-user',
        'methods': ['POST']
    },
    'send_message': {
        'resource': 'user/matches/{id}',
        'docs': 'https://gist.github.com/rtt/10403467#message-sending',
        'methods': ['GET']
    },
    'update_location': {
        'resource': 'user/ping',
        'docs': 'https://gist.github.com/rtt/10403467#updating-your-location',
        'methods': ['GET']
    },
    'updates': {
        'resource': 'updates',
        'docs': 'https://gist.github.com/rtt/10403467#get-updates',
        'methods': ['GET']
    },
    'like': {
        'resource': 'like/{id}',
        'docs': 'https://gist.github.com/rtt/10403467#to-like-or-pass-a-user',
        'methods': ['GET']
    },
    'pass': {
        'resource': 'pass/{id}',
        'docs': 'https://gist.github.com/rtt/10403467#to-like-or-pass-a-user',
        'methods': ['GET']
    },
    'recommendations': {
        'resource': 'user/recs',
        'docs': 'https://gist.github.com/rtt/10403467#recommendations',
        'methods': ['GET']
    }
}
