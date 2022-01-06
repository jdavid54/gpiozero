# need Status board : https://thepihut.com/products/status-board-pro

from gpiozero import StatusBoard, PingServer
sb = StatusBoard()
#print(dir(StatusBoard))

print(sb) #<gpiozero.StatusBoard object containing 5 devices: one, two, three, four, five>
print(sb.one)
print(sb.one.button)
print(sb.one.lights)
print(sb.one.lights.red)
print(sb.one.lights.green)

devices = ['one', 'two', 'three', 'four', 'five']
for dev in devices:
    print(dev)
    print(getattr(sb,dev))
    print(getattr(sb,dev).button)
    print(getattr(sb,dev).lights)
    print(getattr(sb,dev).lights.red)
    print(getattr(sb,dev).lights.green)

    
pi0 = PingServer('192.168.0.184')
print(pi0.is_active)

