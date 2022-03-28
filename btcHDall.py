# =====================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : X4@mmdrza.Com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# =====================================================

from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hexer import mHash
import requests
from colorama import Fore, Style
from lxml import html, etree


def ethtx(addr):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + addr
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def p2shtxx(p2sh):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + p2sh
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def p2wshtxx(p2wsh):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + p2wsh
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

def p2wpkhtxx(p2wpkh):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + p2wpkh
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
    addr = hdwallet.p2pkh_address()
    p2sh = hdwallet.p2sh_address()
    p2wsh = hdwallet.p2wsh_address()
    p2wpkh = hdwallet.p2wpkh_address()
    p2shtx = p2shtxx(p2sh)
    p2wshtx = p2wshtxx(p2wsh)
    p2wpkhtx = p2wpkhtxx(p2wpkh)
    xtxid = ethtx(addr)
    print(Fore.WHITE + str(z) + Fore.RED + ' - ' + Fore.RED + str(addr) + Fore.RED  + ' | ' + Fore.GREEN + str(p2sh) +
          Fore.RED + ' | ' + Fore.YELLOW +  str(p2wsh) + Fore.RED + ' | ' + Fore.BLUE + str(p2wpkh) + Fore.RED +
          '| ' + Fore.RED + 'TXiD = ' + str(xtxid) + '|' + str(p2shtx) + '|' + str(p2wshtx) + '|' + str(
        p2wpkhtx))

    z += 1
    if int(xtxid) or int(p2shtx) or int(p2wshtx) or int(p2wpkhtx) > 0:
        print('Winer Wallet BTC Now \nInformation Wallet :\n\n\n ADDRESS = ', str(addr), 'PRIVATE KEY = ',
              str(priv), '\nBALANCE', str(xtxid))
        f = open("WalletWinnerInfoBTC.txt", "a")
        f.write("\nADDRESS P2PKH = " + str(addr) + "  BALANCE = " + str(xtxid))
        f.write("\nADDRESS P2SH : " + str(p2sh) + " BALANCE = " + str(p2shtx))
        f.write("\nADDRESS P2SH : " + str(p2wsh) + " BALANCE = " + str(p2wshtx))
        f.write("\nADDRESS P2SH : " + str(p2wpkh) + " BALANCE = " + str(p2wpkhtx))
        f.write("\nPRIVATE KEY = " + str(priv))
        f.write("\n================[MMDRZA.CoM]================\n")
        f.close()
        print('\nSaved Information Complete ...[ ------- Mmdrza.Com ------- ]\n')
        continue
