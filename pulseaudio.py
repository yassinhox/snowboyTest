from pulseaudio import lib_pulseaudio
import pasimple
import ctypes

ss = lib_pulseaudio.pa_sample_spec(lib_pulseaudio.PA_SAMPLE_S16LE, 44100, 1)

buf = ctypes.create_string_buffer(4096)

s = pasimple.pa_simple_new(
        None, # server name NULL for default
        "avrvu", # program name
        2, # record
        "alsa_output.pci-0000_00_14.2.analog-stereo.monitor", #device
        "vu-record", 
        ctypes.byref(ss),
        None,
        None,
        None
)

while True:
    ret = pasimple.pa_simple_read(s, ctypes.byref(buf), 4096, None)
    #print ret
    data = buf.raw
    # your processing here