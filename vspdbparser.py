from __future__ import print_function
from HTMLParser import HTMLParser

class VSBDBParser(HTMLParser, object):

    def __init__(self):
        self.track_tags = ['span', 'div']
        # this list is used as a stack to keep track of (tag, id) nesting
        self.tag_id_stack = []
        # flags to track when we are parsing key parts of the page
        self.in_div_sub_content1 = False
        self.in_breadcrumb_area = False
        super(VSBDBParser, self).__init__()

    def handle_starttag(self, tag, attrs):
        """handle_starttag."""
        if tag in self.track_tags:
            dattrs = dict(attrs)
            _id = dattrs.get('id')
            # keep track of nesting for any tags we track and their id on the stack
            self.tag_id_stack.append((tag, _id))
            # Track if we are within either the main content div sub_content1 or the breadcrumb_area
            if tag == 'div' and dattrs.get('id') == 'sub_content1':
                self.in_div_sub_content1 = True
            if tag == 'div' and dattrs.get('id') == 'breadcrumb_area':
                self.in_breadcrumb_area = True
    
    def handle_endtag(self, tag):
        """handle_endtag."""
        if tag in self.track_tags:
            # close out tags we track by popping them off the stack
            popped = self.tag_id_stack.pop()
            # Update tracking flags for special content sections
            if popped[0] == 'div' and popped[1] == 'sub_content1':
                self.in_div_sub_content1 = False
            if popped[0] == 'div' and popped[1] == 'breadcrumb_area':
                self.in_breadcrumb_area = False


    def handle_data(self, data):
        """handle_data."""
        if self.in_div_sub_content1 and not self.in_breadcrumb_area:
            if data.strip() != '' and data.strip() != '.':
                print("%s" % data.strip())