import wx
from gui import guiHelper
from gui.settingsDialogs import SettingsPanel
import config
import addonHandler

addonHandler.initTranslation()
ShowClipboardSection = "ShowClipboard"

class ShowClipboardSettingsPanel(SettingsPanel):
	# Translations for title of panel:
	title = _("Show Clipboard")

	def makeSettings(self, settingsSizer):
		Helper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self.Max_Clipboard_Length_Spin = Helper.addLabeledControl(_("Maximum clipboard length (characters)"), wx.SpinCtrl, min=50, max=500000)
		self.Say_Total_Clipboard_Characters_CheckBox = Helper.addItem(wx.CheckBox(self, label=_("Announce the number of characters when opening the clipboard text")))
		self.Max_Clipboard_Length_Spin.SetValue(config.conf[ShowClipboardSection]["max_clipboard_length"])
		self.Say_Total_Clipboard_Characters_CheckBox.SetValue(config.conf[ShowClipboardSection]["say_total_clipboard_characters"])

	def onSave(self):
		config.conf[ShowClipboardSection]["max_clipboard_length"] = self.Max_Clipboard_Length_Spin.GetValue()
		config.conf[ShowClipboardSection]["say_total_clipboard_characters"] = self.Say_Total_Clipboard_Characters_CheckBox.GetValue()
