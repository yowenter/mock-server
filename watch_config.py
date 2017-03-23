import os
import sys
import time
import threading
import traceback

from itertools import chain


class ReloaderLoop:
    _sleep = staticmethod(time.sleep)

    def __init__(self, extra_files=None, interval=3):
        self.extra_files = set(os.path.abspath(x)
                               for x in extra_files or ())

        self.interval = interval

    def trigger_reload(self, filename):
        pass

    def run(self):
        pass

    def log_reload(self, filename):
        filename = os.path.abspath(filename)
        print 'info', ' * Detected change in %r, reloading' % filename


class ConfigReloaderLoop(ReloaderLoop):
    def trigger_reload(self, filename):
        self.log_reload(filename)
        self._reload_gunicorn()

    def _reload_gunicorn(self):
        try:
            os.system("ps aux |grep gunicorn")

        except Exception as e:
            print "reload gunicorn failure", str(e)

            traceback.print_exc(file=sys.stdout)

    def run(self):
        mtimes = {}
        while 1:
            for filename in chain(self.extra_files):
                try:
                    mtime = os.stat(filename).st_mtime
                except OSError:
                    continue

                old_time = mtimes.get(filename)
                if old_time is None:
                    mtimes[filename] = mtime
                    continue
                elif int(mtime) > int(old_time):
                    self.trigger_reload(filename)
            self._sleep(self.interval)


def main():
    paths = list()
    cwd_dir = os.path.dirname(__file__)
    config_path = os.path.join(cwd_dir, 'routes.cfg')
    json_paths = [os.path.join(cwd_dir, os.path.join("json_files", x))
                  for x in
                  os.listdir(os.path.join(cwd_dir, 'json_files'))]

    paths.append(config_path)
    paths.extend(json_paths)
    print "watching files", paths

    reloader = ConfigReloaderLoop(extra_files=paths)
    reloader.run()


if __name__ == '__main__':
    t = threading.Thread(target=main)
    t.setDaemon(True)
    t.start()
