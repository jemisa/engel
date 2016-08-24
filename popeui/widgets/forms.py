import html

from .base import BaseElement
from ..utils import html_property


class Button(BaseElement):
  """
  A simple button.
  """

  html_tag = "button"

  def build(self, text):
    super(Button, self).build()
    self.content = text


class TextBox(BaseElement):
  """
  A simple textbox.

  **Default Events**:

  ``OnChange`` (client-side)
    Updates the python object to match the client textbox value.
  """

  html_tag = 'input'

  @property
  def text(self):
    return self._text

  @text.setter
  def text(self, value):
    self._text = html.escape(value)
    if self.view and self.view.is_loaded:
      self.view.dispatch({'name': 'text', 'selector': '#' + self.id, 'text': value})

  input_type = html_property('type')
  name = html_property('name')

  def build(self, name=None):
    super(TextBox, self).build()
    self._text = ""
    self.input_type = 'text'

    if name:
      self.name = name

  def on_view_attached(self):
    super(TextBox, self).on_view_attached()

    def text_changed_callback(event, interface):
      self._text = html.escape(event['event_object']['target']['value'])

    self.view.on('change', text_changed_callback, '#' + self.id)
