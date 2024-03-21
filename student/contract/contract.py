# 编辑时间 : 2024/3/18 11:25
from web3 import Web3
from eth_account.account import Account, LocalAccount, SignedTransaction


# 连接到以太坊节点
w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/af53cecd02fc46dbb922fe10a6171eda'))

# 合约地址
contract_address="0x0565c7eA63f097F35380E9801713A89bED09FDf4"

# ABI
contract_abi = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_subject",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_score",
				"type": "uint256"
			}
		],
		"name": "addScore",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			}
		],
		"name": "addStudent",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_studentId",
				"type": "uint256"
			}
		],
		"name": "deleteStudent",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_studentId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_newName",
				"type": "string"
			}
		],
		"name": "modifyStudentName",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_handler",
				"type": "address"
			}
		],
		"name": "setHandler",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_num",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_score",
				"type": "uint256"
			}
		],
		"name": "updateScore",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "admin",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_studentId",
				"type": "uint256"
			}
		],
		"name": "getStudentInfo",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					}
				],
				"internalType": "struct StudentGradeManagement.Student",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_studentId",
				"type": "uint256"
			}
		],
		"name": "getStudentScore",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "subject",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "score",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "appraise",
						"type": "string"
					}
				],
				"internalType": "struct StudentGradeManagement.Score[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "handlers",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "scores",
		"outputs": [
			{
				"internalType": "string",
				"name": "subject",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "score",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "appraise",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "studentCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "students",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

# 创建合约实例
contract_instance = w3.eth.contract(address=contract_address, abi=contract_abi)


# 获取Admin地址
def get_admin():
	return call_contract_view_func("admin")

# 获取学生信息
def get_student_info(id:str):
	return call_contract_view_func("getStudentInfo",id)

# 设置Handler
def set_handler(address: str):
	return call_contract_sign_func(func_name="setHandler",_handler=address)

# 添加学生
def add_student(id:str,name:str):
	return call_contract_sign_func(func_name="addStudent",id=id,name=name)

# 删除学生
def delete_student(id):
	return call_contract_sign_func(func_name="deleteStudent",_id=id)

# 修改学生成绩
def update_student_score(id,num,score):
	return call_contract_sign_func(func_name="updateScore",_id=id,_num=num,_score=score)

# 添加学生成绩
def add_student_score(id,subject,score):
	return call_contract_sign_func(func_name="addScore",_id=id,_subject=subject,_score=score)

# 调用合约非view方法
def call_contract_sign_func(account: LocalAccount,func_name: str,
                            gas=200000, value=0, **kwargs):
    """
    调用合约非View方法
    :param w3: Web3 实例
    :param account: 账户实例
    :param address: 合约地址
    :param abi: 合约ABI
    :param func_name: 合约方法名
    :param gas: 燃气,默认200000
    :param value: 附带转账金额，默认0
    :param kwargs: 方法参数
    :return: 交易哈希字节数组
    """
    contract_instance = w3.eth.contract(address=contract_address, abi=contract_abi)
    func = getattr(contract_instance.functions, func_name)(**kwargs)
    # 构造交易数据
    tx = func.build_transaction({
        'nonce': w3.eth.get_transaction_count(account.address),
        'value': value,
        'gas': gas,
        'gasPrice': w3.eth.gas_price})
    # 签名
    sign_tx: SignedTransaction = account.sign_transaction(tx)
    # 发送
    return w3.eth.send_raw_transaction(sign_tx.rawTransaction)

# 调用合约view方法
def call_contract_view_func(func_name, **kwargs):
    """
    调用合约View方法
    :param w3:Web3实例
    :param address:合约地址
    :param abi:合约ABI
    :param func_name:合约方法名称
    :param kwargs:合约方法参数
    :return:函数执行结果
    """
    func = getattr(contract_instance.functions, func_name)(**kwargs)
    return func.call()
