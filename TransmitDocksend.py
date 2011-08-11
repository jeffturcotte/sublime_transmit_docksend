import sublime
import sublime_plugin
import subprocess

class TransmitDocksendCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		script = """
		on run
			ignoring application responses
				tell application "Transmit"
					open POSIX file "%s"
				end tell
			end ignoring
		end run
		"""

		proc = subprocess.Popen(
			["osascript", "-e", script % self.view.file_name()], 
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE, 
			stderr=subprocess.STDOUT
		)