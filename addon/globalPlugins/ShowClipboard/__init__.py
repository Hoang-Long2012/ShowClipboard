import globalPluginHandler
import ui
import api
import addonHandler
import config
from scriptHandler import script
from globalCommands import SCRCAT_SYSTEM
from logHandler import log
from gui.settingsDialogs import NVDASettingsDialog
from .settings import ShowClipboardSection, ShowClipboardSettingsPanel

addonHandler.initTranslation()
ScriptCategory = SCRCAT_SYSTEM

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()

		config.conf.spec[ShowClipboardSection] = {
			"max_clipboard_length": "integer(default=50000,min=50,max=500000)",
			"say_total_clipboard_characters": "boolean(default=False)"
		}

		if ShowClipboardSettingsPanel not in NVDASettingsDialog.categoryClasses:
			NVDASettingsDialog.categoryClasses.append(ShowClipboardSettingsPanel)

	def terminate(self):
		if ShowClipboardSettingsPanel in NVDASettingsDialog.categoryClasses:
			NVDASettingsDialog.categoryClasses.remove(ShowClipboardSettingsPanel)
		super().terminate()

	def showClipboard(self, isHTML=False):
		try:
			Clipboard_Text = api.getClipData()
		except OSError:
			Clipboard_Text = None

		if not isinstance(Clipboard_Text, str) or not Clipboard_Text.strip():
			ui.message(_("There is no text on the clipboard"))
			return None

		Clipboard_Length = len(Clipboard_Text)
		if Clipboard_Length > config.conf[ShowClipboardSection]["max_clipboard_length"]:
			ui.message(_("The clipboard contains a large amount of text. It is {} characters long").format(Clipboard_Length))
			return None

		try:
			if config.conf[ShowClipboardSection]["say_total_clipboard_characters"]:
				ui.message(_("The clipboard contains {} characters").format(Clipboard_Length))
			ui.browseableMessage(message=Clipboard_Text, title=_("Clipboard text"), isHtml=isHTML)
		except Exception:
			log.exception("Unable to display clipboard")
			ui.message(_("Unable to display clipboard."))

	# Translations doc for show clipboard content script
	@script(description=_("Show your clipboard content in a browseable window."), category=ScriptCategory)
	def script_showClipboard(self, gesture):
		self.showClipboard(isHTML=False)

	# Translations for show clipboard content with html format script
	@script(description=_("Show your clipboard content in a browseable window with html format."), category=ScriptCategory)
	def script_showClipboardHTML(self, gesture):
		self.showClipboard(isHTML=True)

	__gestures = {
		"kb:NVDA+Windows+X": "showClipboard",
		"kb:NVDA+Windows+Shift+X": "showClipboardHTML"
	}