#https://www.linuxjournal.com/article/2156
mkfifo server_data_bus #create name pipe
mkfifo client_data_received_bus 
ls -l > server_data_bus #serve data
cat < data_bus > client_data_received_bus #client consume data