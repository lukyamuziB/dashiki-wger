# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
import json

from rest_framework import status

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from wger.core.models import UserProfile

from wger.core.tests.base_testcase import WorkoutManagerTestCase


class ApiUserTestCase(WorkoutManagerTestCase):
    '''
     Test API user creation
    '''

    def setUp(self):
        user = User.objects.create_user(username='Charles Oduk')
        user.save()
        profile = UserProfile.objects.get(user=user)
        profile.can_create_via_api = True
        profile.save()

        self.payload = {
            'user_id': user.id,
            'username': 'DonnaMwiine',
            'email': 'donnamwiine@gmail.com',
            'password': 'password'
        }

    def test_create_user_via_api(self):
        '''
        Tests the creation of a user via the API
        '''
        response = self.client.post(
            reverse('core:user:usercreation'),
            data=json.dumps(self.payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
