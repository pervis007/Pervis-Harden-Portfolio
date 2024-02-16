import sys


class HardenError(Exception):
    def __init__(self,message="HardenError Says - Value 5 not allowed"):
        self.message=message
        super().__init__(self.message)




while True:
    try:
        value1 = input("Enter Value 1: ")
        value1 = int(value1)

        value2 = input("Enter Value 2: ")
        value2 = int(value2)
        
        if value2 == 5:
            raise(HardenError)
        

        valuedivided = value1/value2
        break
    
    except HardenError as e:
        print(e)
    except Exception as e:
        print(e)
        print("The value entered was invalid.")
    except KeyboardInterrupt:
        sys.exit(0)    
print(valuedivided)




