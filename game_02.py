def main():
    '''
    Getting your name using in-built function called input().
    
    Prints the players name.

    There will be some editing of the code in this part of the workshop
    showing how to declare, assign and call a variable.
    '''
    #print(input("What's your name? > "))
    player_name = input("what's your name? >")

    if __name__ == '__main__':
        print(f"Your name is {player_name}")
        
        what = "knight"
        print(f"Your name is {player_name}. You are a {what}.")

    player_name = "Grace"
    what = "knight"
    f"Hello, {player_name}"
    f"Hello, {player_name}. You are a {what}."    
    
main()