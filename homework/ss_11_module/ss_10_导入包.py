import homework.ss_11_module.ss_message as ss_message


ss_message.send_message.send("hello")

txt = ss_message.receive_message.receive()
print(txt)
