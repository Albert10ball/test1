# encoding = utf-8
__author__ = "Albert"


from token_transfer import getContractTokens

url = "https://public1.nuls.io/jsonrpc"
headers = {"Content-Type": "application/json"}
contract = "NULSd6Hgvzkzkmc6b7c6hjjekuR4BasdG3twL"


res = getContractTokens.get_contract_tokens(url, headers, 142, 10, contract)
address = res[0]
print(address)
