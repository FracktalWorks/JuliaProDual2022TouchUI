# coding=utf-8
from __future__ import absolute_import
__version__ = get_versions()['version']
del get_versions

import octoprint.plugin

# import time
# import subprocess
# from threading import Timer

# class RepeatedTimer(object):
# 	def __init__(self, interval, function, *args, **kwargs):
# 		self._timer = None
# 		self.interval = interval
# 		self.function = function
# 		self.args = args
# 		self.kwargs = kwargs
# 		self.is_running = False
#
# 	def _run(self):
# 		self.is_running = False
# 		self.start()
# 		self.function(*self.args, **self.kwargs)
#
# 	def start(self):
# 		if not self.is_running:
# 			self._timer = Timer(self.interval, self._run)
# 			self._timer.start()
# 			self.is_running = True
#
# 	def stop(self):
# 		if self.is_running:
# 			self._timer.cancel()
# 			self.is_running = False


class JuliaProDual2022TouchUI(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        # self.resetInetrval = int(self._settings.get(["resetInetrval"]))
        self._logger.info("TouchUI Plugin Started")
        # self._worker = RepeatedTimer(self.resetInetrval, self.worker)
        # self._worker.start()

    def get_update_information(self):
        return dict(
            JuliaProDual2022TouchUI=dict(
                displayName="JuliaProDual2022TouchUI",
                displayVersion=self._plugin_version,
                # version check: github repository
                type="github_release",
                user="FracktalWorks",
                repo="JuliaProDual2022TouchUI",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/FracktalWorks/JuliaProDual2022TouchUI/archive/{target_version}.zip"
            )
        )


__plugin_name__ = "Julia Pro Dual 2022 Touch UI"
__plugin_version__ = __version__
__plugin_pythoncompat__ = ">=3,<4"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = JuliaProDual2022TouchUI()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
