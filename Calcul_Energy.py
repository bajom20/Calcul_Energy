class Energy :
    # First, we will define our attributes: power P and time t
    def __init__(self, P, t): # P and t are variables and not fixed values, so put them in parentheses in def
        self.P = P
        self.t = t
    # After the attributes, we move on to the method, which will be used to calculate the energy E, where E = P.t
    def cal(self):
        E = self.P * self.t
        if E  > 1000:
            E = E/1000
            print("The value in E is greater than 1000, we'll present it in kJ, so E =", E)
        else: print("The value of energy in J will be ", E)

# Create an instance of the Energy class
E1 = Energy( 15, 23) #a first calcul of E with P =15 nd t=23
E2= Energy (15,230) # seconde calcul
# waccess the attributes of the instance:
print("If the value of power in Watte is", E1.P, "and the value of time in second is", E1.t)

#Calculating E using the cal() method:
E1.cal()
#SaMe for £2
print("if the value of power in Watts is", E2.P, "and the value of time in second is", E2.t)
E2.cal()
