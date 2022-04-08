import time
from datetime import datetime
import requests
from lxml import html
from colorama import Fore,Style


def timer():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


count = 1
xspeed = input('Insert Sleep Per Transaction Report With Float Number ========================>> ')
while True:
    urlblock = 'https://www.blockchain.com/btc/unconfirmed-transactions'
    respone_block = requests.get(urlblock)
    byte_string_block = respone_block.content
    source_code_block = html.fromstring(byte_string_block)
    xpatchblock_txid = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]'
    xpatchblock_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/span'
    xpatchblock_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[4]/div[2]/span'
    xpatchblock3_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[4]/div[1]/div[2]'
    xpatchblock3_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[4]/div[3]/div[2]/span'
    xpatchblock3_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[4]/div[4]/div[2]/span'
    xpatchblock4_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[5]/div[1]/div[2]'
    xpatchblock4_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[5]/div[3]/div[2]'
    xpatchblock4_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[5]/div[4]/div[2]'
    xpatchblock6_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[6]/div[1]/div[2]'
    xpatchblock6_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[6]/div[3]/div[2]/span'
    xpatchblock6_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[6]/div[4]/div[2]/span'
    xpatchblock7_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[7]/div[1]/div[2]'
    xpatchblock7_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[7]/div[3]/div[2]/span'
    xpatchblock7_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[7]/div[4]/div[2]/span'
    xpatchblock8_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[8]/div[1]/div[2]'
    xpatchblock8_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[8]/div[3]/div[2]/span'
    xpatchblock8_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[8]/div[4]/div[2]/span'
    xpatchblock9_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[9]/div[1]/div[2]'
    xpatchblock9_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[9]/div[3]/div[2]/span'
    xpatchblock9_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[9]/div[4]/div[2]/span'
    xpatchblock10_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[10]/div[1]/div[2]'
    xpatchblock10_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[10]/div[3]/div[2]/span'
    xpatchblock10_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[10]/div[4]/div[2]/span'
    xpatchblock11_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[11]/div[1]/div[2]'
    xpatchblock11_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[11]/div[3]/div[2]/span'
    xpatchblock11_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[11]/div[4]/div[2]/span'
    xpatchblock12_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[12]/div[1]/div[2]'
    xpatchblock12_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[12]/div[3]/div[2]/span'
    xpatchblock12_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[12]/div[4]/div[2]/span'
    xpatchblock13_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[13]/div[1]/div[2]'
    xpatchblock13_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[13]/div[3]/div[2]/span'
    xpatchblock13_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[13]/div[4]/div[2]/span'
    xpatchblock14_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[14]/div[1]/div[2]'
    xpatchblock14_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[14]/div[3]/div[2]/span'
    xpatchblock14_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[14]/div[4]/div[2]/span'
    xpatchblock15_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[15]/div[1]/div[2]'
    xpatchblock15_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[15]/div[3]/div[2]/span'
    xpatchblock15_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[15]/div[4]/div[2]/span'
    xpatchblock16_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[16]/div[1]/div[2]'
    xpatchblock16_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[16]/div[3]/div[2]/span'
    xpatchblock16_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[16]/div[4]/div[2]/span'
    xpatchblock17_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[17]/div[1]/div[2]'
    xpatchblock17_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[17]/div[3]/div[2]/span'
    xpatchblock17_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[17]/div[4]/div[2]/span'
    xpatchblock18_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[18]/div[1]/div[2]'
    xpatchblock18_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[18]/div[3]/div[2]/span'
    xpatchblock18_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[18]/div[4]/div[2]/span'
    xpatchblock19_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[19]/div[1]/div[2]'
    xpatchblock19_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[19]/div[3]/div[2]/span'
    xpatchblock19_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[19]/div[4]/div[2]/span'
    xpatchblock20_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[20]/div[1]/div[2]'
    xpatchblock20_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[20]/div[3]/div[2]/span'
    xpatchblock20_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[20]/div[4]/div[2]/span'
    xpatchblock21_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[21]/div[1]/div[2]'
    xpatchblock21_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[21]/div[3]/div[2]/span'
    xpatchblock21_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[21]/div[3]/div[2]/span'
    xpatchblock22_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[22]/div[1]/div[2]'
    xpatchblock22_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[22]/div[3]/div[2]/span'
    xpatchblock22_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[22]/div[3]/div[2]/span'
    xpatchblock23_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[23]/div[1]/div[2]'
    xpatchblock23_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[23]/div[3]/div[2]/span'
    xpatchblock23_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[23]/div[3]/div[2]/span'
    xpatchblock24_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[24]/div[1]/div[2]'
    xpatchblock24_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[24]/div[3]/div[2]/span'
    xpatchblock24_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[24]/div[3]/div[2]/span'
    xpatchblock25_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[25]/div[1]/div[2]'
    xpatchblock25_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[25]/div[3]/div[2]/span'
    xpatchblock25_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[25]/div[3]/div[2]/span'
    xpatchblock26_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[26]/div[1]/div[2]'
    xpatchblock26_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[26]/div[3]/div[2]/span'
    xpatchblock26_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[26]/div[3]/div[2]/span'
    xpatchblock27_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[27]/div[1]/div[2]'
    xpatchblock27_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[27]/div[3]/div[2]/span'
    xpatchblock27_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[27]/div[3]/div[2]/span'
    xpatchblock28_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[28]/div[1]/div[2]'
    xpatchblock28_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[28]/div[3]/div[2]/span'
    xpatchblock28_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[28]/div[3]/div[2]/span'
    xpatchblock29_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[29]/div[1]/div[2]'
    xpatchblock29_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[29]/div[3]/div[2]/span'
    xpatchblock29_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[29]/div[3]/div[2]/span'
    xpatchblock30_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[30]/div[1]/div[2]'
    xpatchblock30_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[30]/div[3]/div[2]/span'
    xpatchblock30_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[30]/div[3]/div[2]/span'
    xpatchblock31_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[31]/div[1]/div[2]'
    xpatchblock31_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[31]/div[3]/div[2]/span'
    xpatchblock31_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[31]/div[3]/div[2]/span'
    xpatchblock32_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[32]/div[1]/div[2]'
    xpatchblock32_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[32]/div[3]/div[2]/span'
    xpatchblock32_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[32]/div[3]/div[2]/span'
    xpatchblock33_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[33]/div[1]/div[2]'
    xpatchblock33_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[33]/div[3]/div[2]/span'
    xpatchblock33_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[33]/div[3]/div[2]/span'
    xpatchblock34_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[34]/div[1]/div[2]'
    xpatchblock34_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[34]/div[3]/div[2]/span'
    xpatchblock34_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[34]/div[3]/div[2]/span'
    xpatchblock35_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[35]/div[1]/div[2]'
    xpatchblock35_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[35]/div[3]/div[2]/span'
    xpatchblock35_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[35]/div[3]/div[2]/span'
    xpatchblock36_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[36]/div[1]/div[2]'
    xpatchblock36_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[36]/div[3]/div[2]/span'
    xpatchblock36_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[36]/div[3]/div[2]/span'
    xpatchblock37_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[37]/div[1]/div[2]'
    xpatchblock37_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[37]/div[3]/div[2]/span'
    xpatchblock37_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[37]/div[3]/div[2]/span'
    xpatchblock38_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[38]/div[1]/div[2]'
    xpatchblock38_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[38]/div[3]/div[2]/span'
    xpatchblock38_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[38]/div[3]/div[2]/span'
    xpatchblock39_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[39]/div[1]/div[2]'
    xpatchblock39_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[39]/div[3]/div[2]/span'
    xpatchblock39_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[39]/div[3]/div[2]/span'
    xpatchblock40_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[40]/div[1]/div[2]'
    xpatchblock40_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[40]/div[3]/div[2]/span'
    xpatchblock40_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[40]/div[3]/div[2]/span'
    xpatchblock41_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[41]/div[1]/div[2]'
    xpatchblock41_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[41]/div[3]/div[2]/span'
    xpatchblock41_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[41]/div[3]/div[2]/span'
    xpatchblock42_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[42]/div[1]/div[2]'
    xpatchblock42_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[42]/div[3]/div[2]/span'
    xpatchblock42_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[42]/div[3]/div[2]/span'
    xpatchblock43_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[43]/div[1]/div[2]'
    xpatchblock43_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[43]/div[3]/div[2]/span'
    xpatchblock43_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[43]/div[3]/div[2]/span'
    xpatchblock44_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[44]/div[1]/div[2]'
    xpatchblock44_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[44]/div[3]/div[2]/span'
    xpatchblock44_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[44]/div[3]/div[2]/span'
    xpatchblock45_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[45]/div[1]/div[2]'
    xpatchblock45_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[45]/div[3]/div[2]/span'
    xpatchblock45_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[45]/div[3]/div[2]/span'
    xpatchblock46_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[46]/div[1]/div[2]'
    xpatchblock46_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[46]/div[3]/div[2]/span'
    xpatchblock46_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[46]/div[3]/div[2]/span'
    xpatchblock47_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[47]/div[1]/div[2]'
    xpatchblock47_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[47]/div[3]/div[2]/span'
    xpatchblock47_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[47]/div[3]/div[2]/span'
    xpatchblock48_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[48]/div[1]/div[2]'
    xpatchblock48_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[48]/div[3]/div[2]/span'
    xpatchblock48_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[48]/div[3]/div[2]/span'
    xpatchblock49_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[49]/div[1]/div[2]'
    xpatchblock49_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[49]/div[3]/div[2]/span'
    xpatchblock49_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[49]/div[3]/div[2]/span'
    xpatchblock50_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[50]/div[1]/div[2]'
    xpatchblock50_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[50]/div[3]/div[2]/span'
    xpatchblock50_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[50]/div[3]/div[2]/span'

    # =========================================[MMDRZA.COM]=============================================
    blocktreetxid = source_code_block.xpath(xpatchblock_txid)
    blocktree_btc = source_code_block.xpath(xpatchblock_btc)
    blocktree_usd = source_code_block.xpath(xpatchblock_usd)
    blocktree3_hex = source_code_block.xpath(xpatchblock3_hex)
    blocktree4_hex = source_code_block.xpath(xpatchblock4_hex)
    blocktree3_btc = source_code_block.xpath(xpatchblock3_btc)
    blocktree4_btc = source_code_block.xpath(xpatchblock4_btc)
    blocktree3_usd = source_code_block.xpath(xpatchblock3_usd)
    blocktree4_usd = source_code_block.xpath(xpatchblock4_usd)
    blocktree_6_hex = source_code_block.xpath(xpatchblock6_hex)
    blocktree_6_btc = source_code_block.xpath(xpatchblock6_btc)
    blocktree_6_usd = source_code_block.xpath(xpatchblock6_usd)
    blocktree_7_hex = source_code_block.xpath(xpatchblock7_hex)
    blocktree_7_btc = source_code_block.xpath(xpatchblock7_btc)
    blocktree_7_usd = source_code_block.xpath(xpatchblock7_usd)
    blocktree_8_hex = source_code_block.xpath(xpatchblock8_hex)
    blocktree_8_btc = source_code_block.xpath(xpatchblock8_btc)
    blocktree_8_usd = source_code_block.xpath(xpatchblock8_usd)
    blocktree_9_hex = source_code_block.xpath(xpatchblock9_hex)
    blocktree_9_btc = source_code_block.xpath(xpatchblock9_btc)
    blocktree_9_usd = source_code_block.xpath(xpatchblock9_usd)
    blocktree_10_hex = source_code_block.xpath(xpatchblock10_hex)
    blocktree_10_btc = source_code_block.xpath(xpatchblock10_btc)
    blocktree_10_usd = source_code_block.xpath(xpatchblock10_usd)
    blocktree_11_hex = source_code_block.xpath(xpatchblock11_hex)
    blocktree_11_btc = source_code_block.xpath(xpatchblock11_btc)
    blocktree_11_usd = source_code_block.xpath(xpatchblock11_usd)
    blocktree_12_hex = source_code_block.xpath(xpatchblock12_hex)
    blocktree_12_btc = source_code_block.xpath(xpatchblock12_btc)
    blocktree_12_usd = source_code_block.xpath(xpatchblock12_usd)
    blocktree_13_hex = source_code_block.xpath(xpatchblock13_hex)
    blocktree_13_btc = source_code_block.xpath(xpatchblock13_btc)
    blocktree_13_usd = source_code_block.xpath(xpatchblock13_usd)
    blocktree_14_hex = source_code_block.xpath(xpatchblock14_hex)
    blocktree_14_btc = source_code_block.xpath(xpatchblock14_btc)
    blocktree_14_usd = source_code_block.xpath(xpatchblock14_usd)
    blocktree_15_hex = source_code_block.xpath(xpatchblock15_hex)
    blocktree_15_btc = source_code_block.xpath(xpatchblock15_btc)
    blocktree_15_usd = source_code_block.xpath(xpatchblock15_usd)
    blocktree_16_hex = source_code_block.xpath(xpatchblock16_hex)
    blocktree_16_btc = source_code_block.xpath(xpatchblock16_btc)
    blocktree_16_usd = source_code_block.xpath(xpatchblock16_usd)
    blocktree_17_hex = source_code_block.xpath(xpatchblock17_hex)
    blocktree_17_btc = source_code_block.xpath(xpatchblock17_btc)
    blocktree_17_usd = source_code_block.xpath(xpatchblock17_usd)
    blocktree_18_hex = source_code_block.xpath(xpatchblock18_hex)
    blocktree_18_btc = source_code_block.xpath(xpatchblock18_btc)
    blocktree_18_usd = source_code_block.xpath(xpatchblock18_usd)
    blocktree_19_hex = source_code_block.xpath(xpatchblock19_hex)
    blocktree_19_btc = source_code_block.xpath(xpatchblock19_btc)
    blocktree_19_usd = source_code_block.xpath(xpatchblock19_usd)
    blocktree_20_hex = source_code_block.xpath(xpatchblock20_hex)
    blocktree_20_btc = source_code_block.xpath(xpatchblock20_btc)
    blocktree_20_usd = source_code_block.xpath(xpatchblock20_usd)
    # =========================================[MMDRZA.COM]=============================================
    block3btc = str(blocktree3_btc[0].text_content())
    block4hex = str(blocktree4_hex[0].text_content())
    block4btc = str(blocktree4_btc[0].text_content())
    block3usd = str(blocktree3_usd[0].text_content())
    block4usd = str(blocktree4_usd[0].text_content())
    block3hex = str(blocktree3_hex[0].text_content())
    blocktxid = str(blocktreetxid[0].text_content())
    blockbtc = str(blocktree_btc[0].text_content())
    blockusd = str(blocktree_usd[0].text_content())
    chblock1btc = str(blockbtc)[0]
    chblock2btc = str(block3btc)[0]
    chblock3btc = str(block4btc)[0]
    blockhex_6 = str(blocktree_6_hex[0].text_content())
    blockhex_7 = str(blocktree_7_hex[0].text_content())
    blockhex_8 = str(blocktree_8_hex[0].text_content())
    blockhex_9 = str(blocktree_9_hex[0].text_content())
    blockhex_10 = str(blocktree_10_hex[0].text_content())
    blockhex_11 = str(blocktree_11_hex[0].text_content())
    blockhex_12 = str(blocktree_12_hex[0].text_content())
    blockhex_13 = str(blocktree_13_hex[0].text_content())
    blockhex_14 = str(blocktree_14_hex[0].text_content())
    blockhex_15 = str(blocktree_15_hex[0].text_content())
    blockhex_16 = str(blocktree_16_hex[0].text_content())
    blockhex_17 = str(blocktree_17_hex[0].text_content())
    blockhex_18 = str(blocktree_18_hex[0].text_content())
    blockhex_19 = str(blocktree_19_hex[0].text_content())
    blockhex_20 = str(blocktree_20_hex[0].text_content())
    blockbtc_6 = str(blocktree_6_btc[0].text_content())
    blockbtc_7 = str(blocktree_7_btc[0].text_content())
    blockbtc_8 = str(blocktree_8_btc[0].text_content())
    blockbtc_9 = str(blocktree_9_btc[0].text_content())
    blockbtc_10 = str(blocktree_10_btc[0].text_content())
    blockbtc_11 = str(blocktree_11_btc[0].text_content())
    blockbtc_12 = str(blocktree_12_btc[0].text_content())
    blockbtc_13 = str(blocktree_13_btc[0].text_content())
    blockbtc_14 = str(blocktree_14_btc[0].text_content())
    blockbtc_15 = str(blocktree_15_btc[0].text_content())
    blockbtc_16 = str(blocktree_16_btc[0].text_content())
    blockbtc_17 = str(blocktree_17_btc[0].text_content())
    blockbtc_18 = str(blocktree_18_btc[0].text_content())
    blockbtc_19 = str(blocktree_19_btc[0].text_content())
    blockbtc_20 = str(blocktree_20_btc[0].text_content())
    blockusd_6 = str(blocktree_6_usd[0].text_content())
    blockusd_7 = str(blocktree_7_usd[0].text_content())
    blockusd_8 = str(blocktree_8_usd[0].text_content())
    blockusd_9 = str(blocktree_9_usd[0].text_content())
    blockusd_10 = str(blocktree_10_usd[0].text_content())
    blockusd_11 = str(blocktree_11_usd[0].text_content())
    blockusd_12 = str(blocktree_12_usd[0].text_content())
    blockusd_13 = str(blocktree_13_usd[0].text_content())
    blockusd_14 = str(blocktree_14_usd[0].text_content())
    blockusd_15 = str(blocktree_15_usd[0].text_content())
    blockusd_16 = str(blocktree_16_usd[0].text_content())
    blockusd_17 = str(blocktree_17_usd[0].text_content())
    blockusd_18 = str(blocktree_18_usd[0].text_content())
    blockusd_19 = str(blocktree_19_usd[0].text_content())
    blockusd_20 = str(blocktree_20_usd[0].text_content())
    blocktree_21_hex = source_code_block.xpath(xpatchblock21_hex)
    blocktree_21_btc = source_code_block.xpath(xpatchblock21_btc)
    blocktree_21_usd = source_code_block.xpath(xpatchblock21_usd)
    blockhex_21 = str(blocktree_21_hex[0].text_content())
    blockbtc_21 = str(blocktree_21_btc[0].text_content())
    blockusd_21 = str(blocktree_21_usd[0].text_content())
    blocktree_22_hex = source_code_block.xpath(xpatchblock22_hex)
    blocktree_22_btc = source_code_block.xpath(xpatchblock22_btc)
    blocktree_22_usd = source_code_block.xpath(xpatchblock22_usd)
    blockhex_22 = str(blocktree_22_hex[0].text_content())
    blockbtc_22 = str(blocktree_22_btc[0].text_content())
    blockusd_22 = str(blocktree_22_usd[0].text_content())
    blocktree_23_hex = source_code_block.xpath(xpatchblock23_hex)
    blocktree_23_btc = source_code_block.xpath(xpatchblock23_btc)
    blocktree_23_usd = source_code_block.xpath(xpatchblock23_usd)
    blockhex_23 = str(blocktree_23_hex[0].text_content())
    blockbtc_23 = str(blocktree_23_btc[0].text_content())
    blockusd_23 = str(blocktree_23_usd[0].text_content())
    blocktree_24_hex = source_code_block.xpath(xpatchblock24_hex)
    blocktree_24_btc = source_code_block.xpath(xpatchblock24_btc)
    blocktree_24_usd = source_code_block.xpath(xpatchblock24_usd)
    blockhex_24 = str(blocktree_24_hex[0].text_content())
    blockbtc_24 = str(blocktree_24_btc[0].text_content())
    blockusd_24 = str(blocktree_24_usd[0].text_content())
    blocktree_25_hex = source_code_block.xpath(xpatchblock25_hex)
    blocktree_25_btc = source_code_block.xpath(xpatchblock25_btc)
    blocktree_25_usd = source_code_block.xpath(xpatchblock25_usd)
    blockhex_25 = str(blocktree_25_hex[0].text_content())
    blockbtc_25 = str(blocktree_25_btc[0].text_content())
    blockusd_25 = str(blocktree_25_usd[0].text_content())
    blocktree_26_hex = source_code_block.xpath(xpatchblock26_hex)
    blocktree_26_btc = source_code_block.xpath(xpatchblock26_btc)
    blocktree_26_usd = source_code_block.xpath(xpatchblock26_usd)
    blockhex_26 = str(blocktree_26_hex[0].text_content())
    blockbtc_26 = str(blocktree_26_btc[0].text_content())
    blockusd_26 = str(blocktree_26_usd[0].text_content())
    blocktree_27_hex = source_code_block.xpath(xpatchblock27_hex)
    blocktree_27_btc = source_code_block.xpath(xpatchblock27_btc)
    blocktree_27_usd = source_code_block.xpath(xpatchblock27_usd)
    blockhex_27 = str(blocktree_27_hex[0].text_content())
    blockbtc_27 = str(blocktree_27_btc[0].text_content())
    blockusd_27 = str(blocktree_27_usd[0].text_content())
    blocktree_28_hex = source_code_block.xpath(xpatchblock28_hex)
    blocktree_28_btc = source_code_block.xpath(xpatchblock28_btc)
    blocktree_28_usd = source_code_block.xpath(xpatchblock28_usd)
    blockhex_28 = str(blocktree_28_hex[0].text_content())
    blockbtc_28 = str(blocktree_28_btc[0].text_content())
    blockusd_28 = str(blocktree_28_usd[0].text_content())
    blocktree_29_hex = source_code_block.xpath(xpatchblock29_hex)
    blocktree_29_btc = source_code_block.xpath(xpatchblock29_btc)
    blocktree_29_usd = source_code_block.xpath(xpatchblock29_usd)
    blockhex_29 = str(blocktree_29_hex[0].text_content())
    blockbtc_29 = str(blocktree_29_btc[0].text_content())
    blockusd_29 = str(blocktree_29_usd[0].text_content())
    blocktree_30_hex = source_code_block.xpath(xpatchblock30_hex)
    blocktree_30_btc = source_code_block.xpath(xpatchblock30_btc)
    blocktree_30_usd = source_code_block.xpath(xpatchblock30_usd)
    blockhex_30 = str(blocktree_30_hex[0].text_content())
    blockbtc_30 = str(blocktree_30_btc[0].text_content())
    blockusd_30 = str(blocktree_30_usd[0].text_content())
    blocktree_31_hex = source_code_block.xpath(xpatchblock31_hex)
    blocktree_31_btc = source_code_block.xpath(xpatchblock31_btc)
    blocktree_31_usd = source_code_block.xpath(xpatchblock31_usd)
    blockhex_31 = str(blocktree_31_hex[0].text_content())
    blockbtc_31 = str(blocktree_31_btc[0].text_content())
    blockusd_31 = str(blocktree_31_usd[0].text_content())
    blocktree_32_hex = source_code_block.xpath(xpatchblock32_hex)
    blocktree_32_btc = source_code_block.xpath(xpatchblock32_btc)
    blocktree_32_usd = source_code_block.xpath(xpatchblock32_usd)
    blockhex_32 = str(blocktree_32_hex[0].text_content())
    blockbtc_32 = str(blocktree_32_btc[0].text_content())
    blockusd_32 = str(blocktree_32_usd[0].text_content())
    blocktree_33_hex = source_code_block.xpath(xpatchblock33_hex)
    blocktree_33_btc = source_code_block.xpath(xpatchblock33_btc)
    blocktree_33_usd = source_code_block.xpath(xpatchblock33_usd)
    blockhex_33 = str(blocktree_33_hex[0].text_content())
    blockbtc_33 = str(blocktree_33_btc[0].text_content())
    blockusd_33 = str(blocktree_33_usd[0].text_content())
    blocktree_34_hex = source_code_block.xpath(xpatchblock34_hex)
    blocktree_34_btc = source_code_block.xpath(xpatchblock34_btc)
    blocktree_34_usd = source_code_block.xpath(xpatchblock34_usd)
    blockhex_34 = str(blocktree_34_hex[0].text_content())
    blockbtc_34 = str(blocktree_34_btc[0].text_content())
    blockusd_34 = str(blocktree_34_usd[0].text_content())
    blocktree_35_hex = source_code_block.xpath(xpatchblock35_hex)
    blocktree_35_btc = source_code_block.xpath(xpatchblock35_btc)
    blocktree_35_usd = source_code_block.xpath(xpatchblock35_usd)
    blockhex_35 = str(blocktree_35_hex[0].text_content())
    blockbtc_35 = str(blocktree_35_btc[0].text_content())
    blockusd_35 = str(blocktree_35_usd[0].text_content())
    blocktree_36_hex = source_code_block.xpath(xpatchblock36_hex)
    blocktree_36_btc = source_code_block.xpath(xpatchblock36_btc)
    blocktree_36_usd = source_code_block.xpath(xpatchblock36_usd)
    blockhex_36 = str(blocktree_36_hex[0].text_content())
    blockbtc_36 = str(blocktree_36_btc[0].text_content())
    blockusd_36 = str(blocktree_36_usd[0].text_content())
    blocktree_37_hex = source_code_block.xpath(xpatchblock37_hex)
    blocktree_37_btc = source_code_block.xpath(xpatchblock37_btc)
    blocktree_37_usd = source_code_block.xpath(xpatchblock37_usd)
    blockhex_37 = str(blocktree_37_hex[0].text_content())
    blockbtc_37 = str(blocktree_37_btc[0].text_content())
    blockusd_37 = str(blocktree_37_usd[0].text_content())
    blocktree_38_hex = source_code_block.xpath(xpatchblock38_hex)
    blocktree_38_btc = source_code_block.xpath(xpatchblock38_btc)
    blocktree_38_usd = source_code_block.xpath(xpatchblock38_usd)
    blockhex_38 = str(blocktree_38_hex[0].text_content())
    blockbtc_38 = str(blocktree_38_btc[0].text_content())
    blockusd_38 = str(blocktree_38_usd[0].text_content())
    blocktree_39_hex = source_code_block.xpath(xpatchblock39_hex)
    blocktree_39_btc = source_code_block.xpath(xpatchblock39_btc)
    blocktree_39_usd = source_code_block.xpath(xpatchblock39_usd)
    blockhex_39 = str(blocktree_39_hex[0].text_content())
    blockbtc_39 = str(blocktree_39_btc[0].text_content())
    blockusd_39 = str(blocktree_39_usd[0].text_content())
    blocktree_40_hex = source_code_block.xpath(xpatchblock40_hex)
    blocktree_40_btc = source_code_block.xpath(xpatchblock40_btc)
    blocktree_40_usd = source_code_block.xpath(xpatchblock40_usd)
    blockhex_40 = str(blocktree_40_hex[0].text_content())
    blockbtc_40 = str(blocktree_40_btc[0].text_content())
    blockusd_40 = str(blocktree_40_usd[0].text_content())
    blocktree_41_hex = source_code_block.xpath(xpatchblock41_hex)
    blocktree_41_btc = source_code_block.xpath(xpatchblock41_btc)
    blocktree_41_usd = source_code_block.xpath(xpatchblock41_usd)
    blockhex_41 = str(blocktree_41_hex[0].text_content())
    blockbtc_41 = str(blocktree_41_btc[0].text_content())
    blockusd_41 = str(blocktree_41_usd[0].text_content())
    blocktree_42_hex = source_code_block.xpath(xpatchblock42_hex)
    blocktree_42_btc = source_code_block.xpath(xpatchblock42_btc)
    blocktree_42_usd = source_code_block.xpath(xpatchblock42_usd)
    blockhex_42 = str(blocktree_42_hex[0].text_content())
    blockbtc_42 = str(blocktree_42_btc[0].text_content())
    blockusd_42 = str(blocktree_42_usd[0].text_content())
    blocktree_43_hex = source_code_block.xpath(xpatchblock43_hex)
    blocktree_43_btc = source_code_block.xpath(xpatchblock43_btc)
    blocktree_43_usd = source_code_block.xpath(xpatchblock43_usd)
    blockhex_43 = str(blocktree_43_hex[0].text_content())
    blockbtc_43 = str(blocktree_43_btc[0].text_content())
    blockusd_43 = str(blocktree_43_usd[0].text_content())
    blocktree_44_hex = source_code_block.xpath(xpatchblock44_hex)
    blocktree_44_btc = source_code_block.xpath(xpatchblock44_btc)
    blocktree_44_usd = source_code_block.xpath(xpatchblock44_usd)
    blockhex_44 = str(blocktree_44_hex[0].text_content())
    blockbtc_44 = str(blocktree_44_btc[0].text_content())
    blockusd_44 = str(blocktree_44_usd[0].text_content())
    blocktree_45_hex = source_code_block.xpath(xpatchblock45_hex)
    blocktree_45_btc = source_code_block.xpath(xpatchblock45_btc)
    blocktree_45_usd = source_code_block.xpath(xpatchblock45_usd)
    blockhex_45 = str(blocktree_45_hex[0].text_content())
    blockbtc_45 = str(blocktree_45_btc[0].text_content())
    blockusd_45 = str(blocktree_45_usd[0].text_content())
    blocktree_46_hex = source_code_block.xpath(xpatchblock46_hex)
    blocktree_46_btc = source_code_block.xpath(xpatchblock46_btc)
    blocktree_46_usd = source_code_block.xpath(xpatchblock46_usd)
    blockhex_46 = str(blocktree_46_hex[0].text_content())
    blockbtc_46 = str(blocktree_46_btc[0].text_content())
    blockusd_46 = str(blocktree_46_usd[0].text_content())
    blocktree_47_hex = source_code_block.xpath(xpatchblock47_hex)
    blocktree_47_btc = source_code_block.xpath(xpatchblock47_btc)
    blocktree_47_usd = source_code_block.xpath(xpatchblock47_usd)
    blockhex_47 = str(blocktree_47_hex[0].text_content())
    blockbtc_47 = str(blocktree_47_btc[0].text_content())
    blockusd_47 = str(blocktree_47_usd[0].text_content())
    blocktree_48_hex = source_code_block.xpath(xpatchblock48_hex)
    blocktree_48_btc = source_code_block.xpath(xpatchblock48_btc)
    blocktree_48_usd = source_code_block.xpath(xpatchblock48_usd)
    blockhex_48 = str(blocktree_48_hex[0].text_content())
    blockbtc_48 = str(blocktree_48_btc[0].text_content())
    blockusd_48 = str(blocktree_48_usd[0].text_content())
    blocktree_49_hex = source_code_block.xpath(xpatchblock49_hex)
    blocktree_49_btc = source_code_block.xpath(xpatchblock49_btc)
    blocktree_49_usd = source_code_block.xpath(xpatchblock49_usd)
    blockhex_49 = str(blocktree_49_hex[0].text_content())
    blockbtc_49 = str(blocktree_49_btc[0].text_content())
    blockusd_49 = str(blocktree_49_usd[0].text_content())
    blocktree_50_hex = source_code_block.xpath(xpatchblock50_hex)
    blocktree_50_btc = source_code_block.xpath(xpatchblock50_btc)
    blocktree_50_usd = source_code_block.xpath(xpatchblock50_usd)
    blockhex_50 = str(blocktree_50_hex[0].text_content())
    blockbtc_50 = str(blocktree_50_btc[0].text_content())
    blockusd_50 = str(blocktree_50_usd[0].text_content())

    # =========================================[MMDRZA.COM]=============================================

    if len(blockbtc) > int(15):
        print(Fore.YELLOW,str(blocktxid),Fore.WHITE,str(blockbtc),Fore.BLUE,str(blockusd))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blocktxid))
        f.write("\n BTC = " + str(blockbtc))
        f.write("\n USD = " + str(blockusd))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.YELLOW,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE,str(blockbtc),Fore.BLUE,str(blockusd))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(block3btc) > int(15):
        print(Fore.YELLOW,str(block3hex),Fore.WHITE,str(block3btc),Fore.BLUE,str(block3usd))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(block3hex))
        f.write("\n BTC = " + str(block3btc))
        f.write("\n USD = " + str(block3usd))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.RED,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE,str(block3btc),Fore.BLUE,str(block3usd))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)
    time.sleep(float(xspeed))
    if len(block4btc) > int(15):
        print(Fore.YELLOW,str(block4hex),Fore.WHITE,str(block4btc),Fore.BLUE,str(block4usd))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(block4hex))
        f.write("\n BTC = " + str(block4btc))
        f.write("\n USD = " + str(block4usd))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.WHITE,'=====> Check Transaction ',str(count),'<=====>', timer(),Fore.WHITE,str(block4btc),Fore.BLUE,str(block4usd))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_6) > int(15):
        print(Fore.YELLOW, str(blockhex_6), Fore.WHITE, str(blockbtc_6),Fore.BLUE, str(blockusd_6))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_6))
        f.write("\n BTC = " + str(blockbtc_6))
        f.write("\n USD = " + str(blockusd_6))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_6),Fore.BLUE, str(blockusd_6))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_7) > int(15):
        print(Fore.YELLOW, str(blockhex_7), Fore.WHITE, str(blockbtc_7),Fore.BLUE, str(blockusd_7))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_7))
        f.write("\n BTC = " + str(blockbtc_7))
        f.write("\n USD = " + str(blockusd_7))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.RED,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_7),Fore.BLUE, str(blockusd_7))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_8) > int(15):
        print(Fore.YELLOW, str(blockhex_8), Fore.WHITE, str(blockbtc_8),Fore.BLUE, str(blockusd_8))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_8))
        f.write("\n BTC = " + str(blockbtc_8))
        f.write("\n USD = " + str(blockusd_8))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.WHITE,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_8),Fore.BLUE, str(blockusd_8))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_9) > int(15):
        print(Fore.YELLOW, str(blockhex_9), Fore.WHITE, str(blockbtc_9),Fore.BLUE, str(blockusd_9))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_9))
        f.write("\n BTC = " + str(blockbtc_9))
        f.write("\n USD = " + str(blockusd_9))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.RED,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_9),Fore.BLUE, str(blockusd_9))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_10) > int(15):
        print(Fore.YELLOW, str(blockhex_10), Fore.WHITE, str(blockbtc_10),Fore.BLUE, str(blockusd_10))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_10))
        f.write("\n BTC = " + str(blockbtc_10))
        f.write("\n USD = " + str(blockusd_10))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.WHITE,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_10),Fore.BLUE, str(blockusd_10))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_11) > int(15):
        print(Fore.YELLOW, str(blockhex_11), Fore.WHITE, str(blockbtc_11),Fore.BLUE, str(blockusd_11))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_11))
        f.write("\n BTC = " + str(blockbtc_11))
        f.write("\n USD = " + str(blockusd_11))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_11),Fore.BLUE, str(blockusd_11))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_12) > int(15):
        print(Fore.YELLOW, str(blockhex_12), Fore.WHITE, str(blockbtc_12),Fore.BLUE, str(blockusd_12))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_12))
        f.write("\n BTC = " + str(blockbtc_12))
        f.write("\n USD = " + str(blockusd_12))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.RED,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_12),Fore.BLUE, str(blockusd_12))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_13) > int(15):
        print(Fore.YELLOW, str(blockhex_13), Fore.WHITE, str(blockbtc_13),Fore.BLUE, str(blockusd_13))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_13))
        f.write("\n BTC = " + str(blockbtc_13))
        f.write("\n USD = " + str(blockusd_13))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.WHITE,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_13),Fore.BLUE, str(blockusd_13))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_14) > int(15):
        print(Fore.YELLOW, str(blockhex_14), Fore.WHITE, str(blockbtc_14),Fore.BLUE, str(blockusd_14))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_14))
        f.write("\n BTC = " + str(blockbtc_14))
        f.write("\n USD = " + str(blockusd_14))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_14),Fore.BLUE, str(blockusd_14))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_15) > int(15):
        print(Fore.YELLOW, str(blockhex_15), Fore.WHITE, str(blockbtc_15),Fore.BLUE, str(blockusd_15))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_15))
        f.write("\n BTC = " + str(blockbtc_15))
        f.write("\n USD = " + str(blockusd_15))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.RED,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_15),Fore.BLUE, str(blockusd_15))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_16) > int(15):
        print(Fore.YELLOW, str(blockhex_16), Fore.WHITE, str(blockbtc_16),Fore.BLUE, str(blockusd_16))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_16))
        f.write("\n BTC = " + str(blockbtc_16))
        f.write("\n USD = " + str(blockusd_16))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.WHITE,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_16),Fore.BLUE, str(blockusd_16))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_17) > int(15):
        print(Fore.YELLOW, str(blockhex_17), Fore.WHITE, str(blockbtc_17),Fore.BLUE, str(blockusd_17))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_17))
        f.write("\n BTC = " + str(blockbtc_17))
        f.write("\n USD = " + str(blockusd_17))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_17),Fore.BLUE, str(blockusd_17))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_18) > int(15):
        print(Fore.YELLOW, str(blockhex_18), Fore.WHITE, str(blockbtc_18),Fore.BLUE, str(blockusd_18))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_18))
        f.write("\n BTC = " + str(blockbtc_18))
        f.write("\n USD = " + str(blockusd_18))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.RED,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_18),Fore.BLUE, str(blockusd_18))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_19) > int(15):
        print(Fore.YELLOW, str(blockhex_19), Fore.WHITE, str(blockbtc_19),Fore.BLUE, str(blockusd_19))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_19))
        f.write("\n BTC = " + str(blockbtc_19))
        f.write("\n USD = " + str(blockusd_19))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.WHITE,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_19),Fore.BLUE, str(blockusd_19))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))
    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_20))
        f.write("\n BTC = " + str(blockbtc_20))
        f.write("\n USD = " + str(blockusd_20))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_21), Fore.WHITE, str(blockbtc_21),Fore.BLUE, str(blockusd_21))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_21))
        f.write("\n BTC = " + str(blockbtc_21))
        f.write("\n USD = " + str(blockusd_21))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_21),Fore.BLUE, str(blockusd_21))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_22), Fore.WHITE, str(blockbtc_22),Fore.BLUE, str(blockusd_22))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_22))
        f.write("\n BTC = " + str(blockbtc_22))
        f.write("\n USD = " + str(blockusd_22))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_22),Fore.BLUE, str(blockusd_22))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_23), Fore.WHITE, str(blockbtc_23),Fore.BLUE, str(blockusd_23))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_23))
        f.write("\n BTC = " + str(blockbtc_23))
        f.write("\n USD = " + str(blockusd_23))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_24))
        f.write("\n BTC = " + str(blockbtc_24))
        f.write("\n USD = " + str(blockusd_24))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_25))
        f.write("\n BTC = " + str(blockbtc_25))
        f.write("\n USD = " + str(blockusd_25))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_26))
        f.write("\n BTC = " + str(blockbtc_26))
        f.write("\n USD = " + str(blockusd_26))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_27))
        f.write("\n BTC = " + str(blockbtc_27))
        f.write("\n USD = " + str(blockusd_27))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_28))
        f.write("\n BTC = " + str(blockbtc_28))
        f.write("\n USD = " + str(blockusd_28))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_29))
        f.write("\n BTC = " + str(blockbtc_29))
        f.write("\n USD = " + str(blockusd_29))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_30))
        f.write("\n BTC = " + str(blockbtc_30))
        f.write("\n USD = " + str(blockusd_30))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_31))
        f.write("\n BTC = " + str(blockbtc_31))
        f.write("\n USD = " + str(blockusd_31))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_32))
        f.write("\n BTC = " + str(blockbtc_32))
        f.write("\n USD = " + str(blockusd_32))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_33))
        f.write("\n BTC = " + str(blockbtc_33))
        f.write("\n USD = " + str(blockusd_33))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_34))
        f.write("\n BTC = " + str(blockbtc_34))
        f.write("\n USD = " + str(blockusd_34))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_35))
        f.write("\n BTC = " + str(blockbtc_35))
        f.write("\n USD = " + str(blockusd_35))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_36))
        f.write("\n BTC = " + str(blockbtc_36))
        f.write("\n USD = " + str(blockusd_36))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_37))
        f.write("\n BTC = " + str(blockbtc_37))
        f.write("\n USD = " + str(blockusd_37))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_38))
        f.write("\n BTC = " + str(blockbtc_38))
        f.write("\n USD = " + str(blockusd_38))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_39))
        f.write("\n BTC = " + str(blockbtc_39))
        f.write("\n USD = " + str(blockusd_39))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))

    if len(blockbtc_20) > int(15):
        print(Fore.YELLOW, str(blockhex_20), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        f = open("Report.txt","a")
        f.write("\nTXiD = " + str(blockhex_40))
        f.write("\n BTC = " + str(blockbtc_40))
        f.write("\n USD = " + str(blockusd_40))
        f.write("\n-----------(M M D R Z A . C o M)-----------")
        f.close()
    else:
        print(Fore.GREEN,'=====> Check Transaction ',str(count),'<=====>', timer(), Fore.WHITE, str(blockbtc_20),Fore.BLUE, str(blockusd_20))
        count += 1
        print(Fore.YELLOW,'----------------------------------------------------------------------',Style.RESET_ALL)

    time.sleep(float(xspeed))


    continue
