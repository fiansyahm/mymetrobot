import telebot	

bot = telebot.TeleBot('5399142793:AAFA9oH7hre7sf-GB_KaE-eAT0gGsLCBtAE')
@bot.message_handler(commands=['start'])
def welcome(message):
    # membalas pesan
    # send="Halo, Selamat Menikmati Layanan Kami"+"\n"
    # +"Command: [Nama Metro]_[Password]"+"\n"+"\n"+"Ex: ME-D5-KD_passwordku1234"+"\n"
    send="Selamat datang di layanan pulsa kami"+"\n"
    bot.reply_to(message,send)

@bot.message_handler(commands=['help'])
def help(message):
    # membalas pesan
    # send="Halo, Selamat Menikmati Layanan Kami"+"\n"
    # +"Command: [Nama Metro]_[Password]"+"\n"+"\n"+"Ex: ME-D5-KD_passwordku1234"+"\n"
    send="Halo, Selamat Menggunakan Layanan Bot Network"+"\n"+"\n"+"Fitur 1: /portidle [Nama Metro]_[Password]"+"\n"+"Ex: /portidle ME-D5-KD_passwordku1234"+"\n"+"\n"+"Fitur 2: /zoc [Nama Metro]_[Password]_[command]"+"\n"+"Ex: /zoc ME-D5-KD_passwordku1234_disp ver"+"\n"
    bot.reply_to(message,send)

@bot.message_handler(commands=['portidle'])
def portidle(message):
    tmp=message.text.split('/portidle ')
    tmp1=tmp[1].split('_')
    # try:
    #     hasil=metro(tmp1[0],0,tmp1[1],'on','on')
    # except:
    #      hasil=metro(tmp1[0],1,tmp1[1],'on','on')
    # send="Port - Port Bandwith - Bandwith - Distance"+"\n"
    # for i,j,k,l in hasil:
    #     send=send+i+" - "+j+" - "+k+" - "+l+"\n"
    # print("hasil"+send)
    bot.reply_to(message,message.text)


    
while True:
    try:
        bot.polling()
    except:
        pass


