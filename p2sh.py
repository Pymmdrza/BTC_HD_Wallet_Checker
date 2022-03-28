from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hexer import mHash
import requests
from colorama import Fore,Style
from lxml import html,etree


def BalTx(addr):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


z = 1
while True:
    hex64 = mHash()
    PRIVATE_KEY: str = hex64
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_private_key(private_key=PRIVATE_KEY)
    priv = hdwallet.private_key()
    addr = hdwallet.p2sh_address()
    xtxid = BalTx(addr)
    print(Fore.WHITE,str(z),Fore.YELLOW,'Address =',Fore.RED,str(addr),Fore.BLUE,'|',Fore.GREEN,' txid =',Fore.WHITE,str(xtxid))
    z += 1
    if int(xtxid) > 0:
        print('Winer Wallet BTC Now \nInformation Wallet :\n\n\n ADDRESS = ',str(addr),'PRIVATE KEY = ',str(priv),
            '\nBALANCE',str(xtxid))
        f = open("WalletWinnerInfoBTC.txt","a")
        f.write("\nADDRESS  = " + str(addr) + "  BALANCE = " + str(xtxid))
        f.write("\nPRIVATE KEY = " + str(priv))
        f.write("\n================[MMDRZA.CoM]================\n")
        f.close()
        print('\nSaved Information Complate ...[ ------- Mmdrza.Com ------- ]\n')
