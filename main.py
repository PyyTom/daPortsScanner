import socket,flet as fl
def main(page:fl.Page):
    def xit(e):
        page.window_destroy()
    def start(e):
        for port in range(65535):
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result=sock.connect_ex((ip.value,port))
            if result==0:
                c_status.controls.append(fl.Text('PORT OPEN - '+str(port)))
                sock.close()
            else:
                c_status.controls.append(fl.Text('PORT CLOSED - '+str(port)))
            page.update()
    ip=fl.TextField(label='INSERT IP')
    c_status=fl.Column(scroll=fl.ScrollMode.ALWAYS,auto_scroll=True)
    page.add(fl.Text('PORTS SCANNER'),
             ip,
             fl.Row(controls=[fl.ElevatedButton('START',on_click=start),
                              fl.ElevatedButton('EXIT',on_click=xit)]),
             c_status)
fl.app(target=main)