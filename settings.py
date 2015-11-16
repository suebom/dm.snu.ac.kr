# -*- coding: utf-8 -*-

import os


CONTACT = {
    'address_ko': '서울시 관악구 관악로 1 서울대학교 39동 339호',
    'address_en': '39-339, Seoul National University, Gwanak-ro, Gwanak-gu, Seoul, South Korea (Zipcode: 151-742)',
    'email': 'datamining@snu.ac.kr',
    'phone': '+82-(0)2-880-7025',
}

MENUS = [
    'datamining',
    'people',
    ('research', ['methods', 'reports', 'publications']),
    ('development', ['sponsors', 'FAQ']),
    'education',
    'courses',
    'admission',
    'software',
    'contact'
]

BABEL = {
    'default_locale': 'ko',
}

LOCALES = ['ko', 'en']

SERVER = {
    'host': '0.0.0.0',
    'port': 8088,
    'debug': True,
}

APP_URL = 'http://dm.snu.ac.kr'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_TEMPLATES = os.path.join(APP_ROOT, 'templates')
