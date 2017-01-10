#!/usr/bin/env python
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

"""Python MadMimi client library."""

__author__ = ('tav@espians.com (tav),'
        'jordan.bouvier@analytemedia.com (Jordan Bouvier)')
__maintainer__ = 'jordan.bouvier@analytemedia.com (Jordan Bouvier)'

import csv
import logging

try:
    from cStringIO import StringIO
except ImportError:
    #from StringIO import StringIO
    from io import StringIO
try:
    from urllib import quote, urlencode
except ImportError:
    from urllib.parse import quote, urlencode

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

try:
    from xml.etree import cElementTree as ElementTree
except ImportError:
    try:
        import cElementTree as ElementTree
    except ImportError:
        try:
            from xml.etree import ElementTree
        except ImportError:
            from elementtree import ElementTree

from yaml import dump, safe_dump


DEFAULT_CONTACT_FIELDS = ('first name', 'last_name', 'email', 'tags')

def parse_lists(response):
    tree = ElementTree.ElementTree()
    lists = {}
    tree.parse(StringIO(response))
    for elem in list(tree.getiterator('list')):
        lists[elem.attrib['name']] = MailingList(elem.attrib['id'],
                                                 elem.attrib['name'],
                                                 elem.attrib['subscriber_count'])

    return lists


class MailingList(object):
    """The main mailing list object."""
    def __init__(self, list_id=0, list_name="", subscribers=0):
        self.subscribers = subscribers
        self.id = list_id
        self.name = list_name

    def __unicode__(self):
        return u"<MailingList: %s>" % self.name

    def __repr__(self):
        return "<MailingList: %s>" % self.name


class MadMimi(object):
    """
    The client is straightforward to use:

      >>> mimi = MadMimi('user@foo.com', 'account-api-key')

    You can use it to list existing lists:

      >>> mimi.lists()
      {'test': <MailingList: test>}

      >>> mimi.lists()["test"].subscribers
      3

      >>> mimi.lists()["test"].name
      "test"

    Delete any of them:

      >>> mimi.delete_list('test')

    Create new ones:

      >>> mimi.add_list('ampify')

    Add new contacts:

      >>> mimi.add_contact(['Tav', 'Espian', 'tav@espians.com'])

    Subscribe contacts to a list:

      >>> mimi.subscribe('tav@espians.com', 'ampify')

    See what lists a contact is subscribed to:

      >>> mimi.subscriptions('tav@espians.com')
      <lists>
        <list subscriber_count="1" name="ampify" id="77461"/>
      </lists>

    And, of course, unsubscribe a contact from a list:

      >>> mimi.unsubscribe('tav@espians.com', 'ampify')

      >>> mimi.subscriptions('tav@espians.com')
      <lists>
      </lists>

    Send a transactional email:

        >>> mimi.send_message('John Doe','johndoe@gmail.com','Promotion Name',
        ...     'Subject of the message','sender@email.com',
        ...     {'var1':'This will go to the template'})
        '1146680279'

    Send an email to a list:

        >>> mimi.send_message_to_list('List Name', 'Promotion Name',
        ...     {'var1':'This will go to the template'})
        '1223645'

    """

    base_url = 'http://api.madmimi.com/'
    secure_base_url = 'https://api.madmimi.com/'

    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

        self.urlopen = urlopen
        self.logger = logging.getLogger('madmimi')
        self.logger.setLevel(logging.WARNING)

    def _get(self, method, **params):
        """Issue a GET request to Madmimi.

        Arguments:
            method: The path to the API method you are accessing, relative
                to the site root.
            is_secure: If is_secure is True, the GET request will be issued
                to MadMimi's secure server.

        Returns:
            The result of the HTTP request as a string.
        """
        is_secure = params.get('is_secure')
        if is_secure:
            url = self.secure_base_url
        else:
            url = self.base_url
        params['username'] = self.username
        params['api_key'] = self.api_key
        url = url + method + '?' + urlencode(params)
        self.logger.debug('get url: %s' % url)

        response = self.urlopen(url).read()
        self.logger.debug('response: %s' % response)
        return response

    def _post(self, method, **params):
        """Issue a POST request to Madmimi.

        Arguments:
            method: The path to the API method you are accessing, relative
                to the site root.
            is_secure: If is_secure is True, the GET request will be issued
                to MadMimi's secure server.

        Returns:
            The result of the HTTP request as a string.
        """
        is_secure = params.get('is_secure')
        if is_secure:
            url = self.secure_base_url + method
        else:
            url = self.base_url + method
        params['username'] = self.username
        params['api_key'] = self.api_key
        if params.get('sender'):
            params['from'] = params['sender']
        
        self.logger.debug('post url: %s' % url)
        self.logger.debug('params: %s' % params)

        response = self.urlopen(url, urlencode(params).encode('utf-8')).read()
        self.logger.debug('response: %s' % response)
        return response

    def lists(self, as_xml=False):
        """Get a list of audience lists.

        Arguments:
            as_xml: If true, the result will be the raw XML response. If False
                the result will be a python dictionary of lists.
                Default is True. (Optional)

        Returns:
            The raw XML response or a dictionary of list names and objects.
            {'list name': <list object>, 'list2 name': <list object>}
        """
        response = self._get('audience_lists/lists.xml')
        if as_xml:
            return response
        else:
            return parse_lists(response)

    def add_list(self, name):
        """Add a new audience list.

        Arguments:
            name: The name of the audience list to add.

        Returns:
            Nothing. The API doesn't provide a response.
        """

        self._post('audience_lists', name=name)

    def delete_list(self, name):
        """Delete an audience list.

        Arguments:
            name: The name of the audience list to delete.

        Returns:
            Nothing. The API doesn't provide a response.
        """

        self._post('audience_lists/%s' % quote(name), _method='delete')

    def add_contacts(self, contacts_data, fields=DEFAULT_CONTACT_FIELDS,
                     audience_list=None):
        """Add audience members to your database.

        Arguments:
            contacts_data: A list of tuples containting contact data.
            fields: A tuple containing the fields that will be represented.

        Returns:
            Nothing. The API doesn't provide a response.
        """

        contacts = []
        contacts.append((fields))
        contacts.extend(contacts_data)

        csvdata = StringIO()
        writer = csv.writer(csvdata)
        [writer.writerow(row) for row in contacts]

        self._post('audience_members', csv_file=csvdata.getvalue(),
                   audience_list=audience_list)

    def subscribe(self, email, audience_list):
        """Add an audience member to an audience list.

        Arguments:
            email: The email address to add to a list.
            audience_list: The audience list to add the email address to.

        Return:
            Nothing. The API doesn't provide a response.
        """

        url = 'audience_lists/%s/add' % quote(audience_list)

        self._post(url, email=email)

    def unsubscribe(self, email, audience_list):
        """Remove an audience member from an audience list.

        Arguments:
            email: The email address to add to a list.
            audience_list: The audience list to add the email address to.

        Returns:
            Nothing. The API doesn't provide a response.
        """

        url = 'audience_lists/%s/remove' % quote(audience_list)

        self._post(url, email=email)

    def subscriptions(self, email, as_xml=False):
        """Get an audience member's current subscriptions.

        Arguments:
            email: The email address to look up.
            as_xml: If true, the result will be the raw XML response. If False
                the result will be a python dictionary of lists.
                Default is True. (Optional)

        Returns:
            The raw XML response or a dictionary of list names and objects of which
            the person is a member.
            {'list name': <list object>, 'list2 name': <list object>}
        """
        response = self._get('audience_members/%s/lists.xml' % quote(email))
        if as_xml:
            return response
        else:
            return parse_lists(response)

    def send_message(self, name, email, promotion, subject, sender, body={},
            raw_html=None, raw_plain_text=None):
        """Sends a message to a user.
        
        Arguments:
            name: Name of the person you are sending to.
            email: Email address of the person you are sending to.
            promotion: Name of the Mad Mimi promotion to send.
            subject: Subject of the email.
            sender: Email address the email should appear to be from.
            
            Only one of body, raw_html or raw_plain_text should be provided.
            Order of preference is html, plain text, body.
            body: Optional. Dict holding variables for the promotion template.
                    {'variable': 'Replcement value'}
            raw_html: Optional. If you want to send a message where the
                promotion doesn't already exist. Make sure the promotion
                name is unique.
            raw_plain_text: Optional. Same as raw_html except it is plain
                text.
        
        Returns:
            The transaction id of the message if successful.
            The error if unsuccessful.
        """
        recipients = "%s <%s>" % (name, email)
        
        if raw_html:
            post = self._post('mailer', promotion_name=promotion,
                    recipients=recipients, subject=subject, sender=sender,
                    raw_html=raw_html, is_secure=True)
        elif raw_plain_text:
            post = self._post('mailer', promotion_name=promotion,
                    recipients=recipients, subject=subject, sender=sender,
                    raw_plain_text=raw_plain_text, is_secure=True)
        else:
            # The YAML dump will fail if it encounters non-strings
            for item, value in body.iteritems():
                body[item] = str(value)
            body = safe_dump(body) # to avoid !!python/str tags by dump(body)
            
            post = self._post('mailer', promotion_name=promotion,
                    recipients=recipients, subject=subject, sender=sender,
                    body=body, is_secure=True)
        
        return post
    
    def send_message_to_list(self, list_name, promotion, body={}):
        """Send a promotion to a subscriber list.

        Arguments:
            list_name: Name of the subscriber list to send the promotion to.
            promotion: Name of the Mad Mimi promotion to send.
            body: Dict holding variables for the promotion template.
                    {'variable': 'Replcement value'}

        Returns:
            The transaction id of the message if successful.
            The error if unsuccessful.
        """

        # The YAML dump will fail if it encounters non-strings
        for item, value in body.iteritems():
            body[item] = str(value)

        body = safe_dump(body) # to avoid !!python/str tags by dump(body)

        return self._post('mailer/to_list', promotion_name=promotion,
                list_name=list_name, body=body, is_secure=True)

    def message_status(self, transaction_id):
        """Get the status of a message.

        Arguments:
            transaction_id: The transaction id of the message you want to
                    get the status for.

        Returns:
            One of the following strings:
                ignorant
                sending
                failed
                sent
                received
                clicked_through
                bounced
                retried
                retry_failed
                abused
        """

        url = 'mailers/status/%s' % transaction_id

        return self._get(url, is_secure=True)

    def supressed_since(self, date):
        """Get a list of email addresses that have opted out since date.

        Arguments:
            date: Python datetime to retrieve opt outs since.
        """

        url = 'audience_members/suppressed_since/%s.txt' % date.strftime('%s')

        return self._get(url)

    def promotion_stats(self):
        """Get an XML document containing stats for all your promotions."""

        return self._get('promotions.xml')
