import requests

url = "https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/create-or-update?tabs=HTTP#code-try-0"

headers = {"Content-Type": "application/json; charset=utf-8"}

data = {
		"properties": {
			"publicIPAllocationMethod": "Static",
			"idleTimeoutInMinutes": 10,
			"publicIPAddressVersion": "IPv4"
		},
		"sku": {
			"name": "Basic"
		},
		"location": "westeurope"
	}

response = requests.post(url, json=data)

print("Status Code", response.status_code)

url2 = "https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/create-or-update?tabs=HTTP#code-try-0"

headers2 = {"Content-Type": "application/json; charset=utf-8"}

data2 = {
    "name": "lab0-2973_z1",
    "id": "/subscriptions/b5189791-6f56-419b-9fe2-10453b314ece/resourceGroups/Groupone/providers/Microsoft.Network/networkInterfaces/lab0-2973_z1",
    "etag": "W/\"1048cbb8-f2e4-4e34-92a0-0ffd5dfbc52f\"",
    "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "36904f97-00f7-4e8c-8320-c9830f54f133",
        "ipConfigurations": [
            {
                "name": "ipconfig1",
                "id": "/subscriptions/b5189791-6f56-419b-9fe2-10453b314ece/resourceGroups/Groupone/providers/Microsoft.Network/networkInterfaces/lab0-2973_z1/ipConfigurations/ipconfig1",
                "etag": "W/\"1048cbb8-f2e4-4e34-92a0-0ffd5dfbc52f\"",
                "type": "Microsoft.Network/networkInterfaces/ipConfigurations",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateIPAddress": "10.0.0.5",
                    "privateIPAllocationMethod": "Dynamic",
                    "publicIPAddress": {
                        "name": "LAB0-2-ip",
                        "id": "/subscriptions/b5189791-6f56-419b-9fe2-10453b314ece/resourceGroups/Groupone/providers/Microsoft.Network/publicIPAddresses/LAB0-2-ip",
                        "properties": {
                            "provisioningState": "Succeeded",
                            "resourceGuid": "45d2a9b2-9236-4bc8-8c73-1aaf8ffe64f2",
                            "publicIPAddressVersion": "IPv4",
                            "publicIPAllocationMethod": "Dynamic",
                            "idleTimeoutInMinutes": 4,
                            "ipTags": [],
                            "ipConfiguration": {
                                "id": "/subscriptions/b5189791-6f56-419b-9fe2-10453b314ece/resourceGroups/Groupone/providers/Microsoft.Network/networkInterfaces/lab0-2973_z1/ipConfigurations/ipconfig1"
                            },
                            "deleteOption": "Detach"
                        },
                        "type": "Microsoft.Network/publicIPAddresses",
                        "sku": {
                            "name": "Basic",
                            "tier": "Regional"
                        }
                    },
                    "subnet": {
                        "id": "/subscriptions/b5189791-6f56-419b-9fe2-10453b314ece/resourceGroups/Groupone/providers/Microsoft.Network/virtualNetworks/Groupone-vnet/subnets/default"
                    },
                    "primary": True,
                    "privateIPAddressVersion": "IPv4"
                }
            }
        ],
        "dnsSettings": {
            "dnsServers": [],
            "appliedDnsServers": [],
            "internalDomainNameSuffix": "oizxcbz3nf0ejmzhmxv3332vig.ax.internal.cloudapp.net"
        },
        "macAddress": "60-45-BD-93-2C-75",
        "enableAcceleratedNetworking": True,
        "vnetEncryptionSupported": False,
        "enableIPForwarding": False,
        "networkSecurityGroup": {
            "id": "/subscriptions/b5189791-6f56-419b-9fe2-10453b314ece/resourceGroups/Groupone/providers/Microsoft.Network/networkSecurityGroups/LAB0-2-nsg"
        },
        "primary": True,
        "virtualMachine": {
            "id": "/subscriptions/b5189791-6f56-419b-9fe2-10453b314ece/resourceGroups/Groupone/providers/Microsoft.Compute/virtualMachines/LAB0-2"
        },
        "hostedWorkloads": [],
        "tapConfigurations": [],
        "nicType": "Standard"
    },
    "type": "Microsoft.Network/networkInterfaces",
    "location": "westeurope",
    "kind": "Regular"
}

response2 = requests.post(url2, json=data)

print("Status Code", response2.status_code)


url3 = "https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/create-or-update?tabs=HTTP&tryIt=true&source=docs#code-try-0"

headers = {"Content-Type": "application/json; charset=utf-8"}

data3 = {
    "name": "LAB0-2",
    "id": "/subscriptions/b5189791-6f56-419b-9fe2-10453b314ece/resourceGroups/Groupone/providers/Microsoft.Compute/virtualMachines/LAB0-2",
    "type": "Microsoft.Compute/virtualMachines",
    "location": "westeurope",
    "properties": {
        "vmId": "6c3df7d3-4c45-4d52-a390-c59bd41a9161",
        "hardwareProfile": {
            "vmSize": "Standard_D2s_v3"
        },
        "storageProfile": {
            "imageReference": {
                "publisher": "canonical",
                "offer": "0001-com-ubuntu-server-focal",
                "sku": "20_04-lts-gen2",
                "version": "latest"
            },
            "osDisk": {
                "osType": "Linux",
                "name": "LAB0-2_disk1_188c8082e5564d9ca2a3ce4ed9c2a4eb",
                "createOption": "FromImage",
                "caching": "ReadWrite",
                "managedDisk": {
                    "storageAccountType": "Premium_LRS",
                    "id": "/subscriptions/b5189791-6f56-419b-9fe2-10453b314ece/resourceGroups/GROUPONE/providers/Microsoft.Compute/disks/LAB0-2_disk1_188c8082e5564d9ca2a3ce4ed9c2a4eb"
                },
                "diskSizeGB": 30
            },
            "dataDisks": []
        },
        "osProfile": {
            "computerName": "LAB0-2",
            "adminUsername": "caoimhehennessy",
            "linuxConfiguration": {
                "disablePasswordAuthentication": True,
                "ssh": {
                    "publicKeys": [
                        {
                            "path": "/home/caoimhehennessy/.ssh/authorized_keys",
                            "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCq+K6aurbWhapB1GNP8vmE85+9gpuwNXt2xoB87Gq8CVBm1TNxf8pUTKKS5uj+bi+vPtyT9IvnyW8QfRzbjmKjbYdukN7n1ufKGg8G6D68dFhuZxF94jmSUTv5COffoBYmZgEPgCazUKyTwn65OE6iucMbqWY77r5h/qTc64V8KoWtKT7GTocyV4MsCG+o0rXFej6SfVZS3Paabjbn5Qyp+2pcUb1xNJ1AQz0M/u/XnnrixKyUADPguyqH+lFJy0R628ANJG7nr/vV6YP0M4NxjZ0xk/jNARTmU8Cx7fZZPt3a/ocP6t+8szqX3qb1Z6j2pzhESWtXA7FhbIPTeL4jq7j4xR2JvhmMBN+7LeDIIIk00VJw7f8gksPDbsgzVRUzjyrjTIPTjbYXSRA2jdpC3Z4zhR4h2ry3vhZ99cunhzOyqV5bh07fiVTK7bGrSHp7EpmigfHexrzpXhptZGt7gH1DyYpNcZBax2drANN9D+3+wJLdbC4wCX0Qtk6Suk0= caoimhehennessy@CAOIMHEHENN9FD3\n"
                        }
                    ]
                }
            },
            "secrets": []
        },
        "networkProfile": {
            "networkInterfaces": [
                {
                    "id": "/subscriptions/b5189791-6f56-419b-9fe2-10453b314ece/resourceGroups/Groupone/providers/Microsoft.Network/networkInterfaces/lab0-2973_z1",
                    "properties": {
                        "deleteOption": "Detach"
                    }
                }
            ]
        },
        "diagnosticsProfile": {
            "bootDiagnostics": {
                "enabled": True
            }
        },
        "provisioningState": "Succeeded"
    },
    "zones": [
        "1"
    ]
}

response3 = requests.post(url, json=data)

print("Status Code", response3.status_code)
