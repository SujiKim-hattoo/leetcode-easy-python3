class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_list = list(address)
        # for loop to find out period
        for i in range(0, len(address_list)):
            if address_list[i] == '.':
                address_list[i] = '[.]'

        # turn list type into string type        
        new_address = ''.join(address_list)
        
        return new_address