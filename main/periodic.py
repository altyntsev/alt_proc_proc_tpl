from _init import script
import alt_proc.time

script.start()

print('Periodic')

script.emit_event('event_tpl', alt_proc.time.now())

script.exit()


