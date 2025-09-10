__package__ = "4. String"

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

if __name__ == "__main__":
    address = input("Enter an IP address: ")

    solution = Solution()
    result = solution.defangIPaddr(address)

    print("\nDefanged IP address:")
    print(result)
