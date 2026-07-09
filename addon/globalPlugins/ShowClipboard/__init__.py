import globalPluginHandler
import ui
import api
import addonHandler
from scriptHandler import script
from globalCommands import SCRCAT_SYSTEM

addonHandler.initTranslation()
ScriptCategory = SCRCAT_SYSTEM

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translations doc for show clipboard script
	@script(description=_("Show your clipboard content."), category=ScriptCategory)
	def script_showClipboard(self, gesture):
		Clipboard_Text = api.getClipData()
		if not isinstance(Clipboard_Text, str):
			ui.message(_("Clipboard is not text.")

		# Translations for window title
		Title = _("Clipboard text")

		try:
			ui.browseableMessage(message=Clipboard_Text, title=Title)
		except:
			ui.message(_("Cannot display clipboard.")

	__gestures = {
		"kb:NVDA+Windows+X": "showClipboard"
	}