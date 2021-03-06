"""
card including user info of the name, tel, age, uid.
features : add, delete, modify, view
"""

# card_func_version


def show_msg():
    """Show prompt message"""
    print('=======================')
    print('1.add card')
    print('2.delete card')
    print('3.modify card')
    print('4.view card')
    print('5.view all card')
    print('0.quit')
    print('=======================')


def add():
    """command 1 - add a card"""

    user_uid = input("Please input your uid: ")  # get info  str
    user_name = input("Please input your name: ")  # str
    user_age = input("Please input your age: ")  # str
    user_tel = input("Please input your tel: ")  # str
    # save a dirt
    user_dirt = {'uid': user_uid, 'name': user_name, 'age': user_age, 'tel': user_tel}
    # append to card_list
    card_list.append(user_dirt)


def delete():
    """command 2 - delete a specified card"""

    if not card_list:  # when prior to command 2
        print('# empty card, please prior to add ! #')
        return  # can back to call function
    # select id
    rm_id = input("select id to del: ")
    for tmp in card_list:  # when traverse is empty, the code in the indentation does not execute
        if tmp['uid'] == rm_id:
            card_list.remove(tmp)
            break  # delete done
    else:
        print('no find uid: %s' % rm_id)


def modify():
    """command 3 - modify a specified card"""

    if not card_list:  # when prior to command 3
        print('# empty card, please prior to add ! #')
        return
    # select id
    ch_id = input("select id to modify(straight to Enter - no modify the member of a card): ")
    for tmp in card_list:
        if tmp['uid'] == ch_id:
            user_name = input("Please input your name: ")  # str
            user_age = input("Please input your age: ")  # str
            user_tel = input("Please input your tel: ")  # str
            if user_name:  # Enter lead to no modify
                tmp['name'] = user_name
            if user_age:
                tmp['age'] = user_age
            if user_tel:
                tmp['tel'] = user_tel
            break  # modify done
    else:
        print('no find uid: %s' % ch_id)


def view():
    """command 4 - view a specified card"""

    if not card_list:  # when prior to command 4
        print('# empty card, please prior to add ! #')
        return
    # select id
    vw_id = input("select id to view: ")
    for tmp in card_list:
        if tmp['uid'] == vw_id:
            print('uid: %s\t name: %s\t age: %s\t tel: %s' % (tmp['uid'], tmp['name'], tmp['age'], tmp['tel']))
            break  # view done
    else:
        print('no find uid: %s' % vw_id)


def view_all():
    """command 5 - view all card"""

    if not card_list:  # when prior to command 5
        print('# empty card, please prior to add ! #')
        return
    for tmp in card_list:  # when traverse is empty, the code in the indentation does not execute
        print('uid: %s\t name: %s\t age: %s\t tel: %s' % (tmp['uid'], tmp['name'], tmp['age'], tmp['tel']))


def ch_cmd(command):
    """choose user command"""

    if command == '1':  # command 1
        # add
        add()

    elif command == '2':  # command 2
        # delete
        delete()

    elif command == '3':  # command 3
        # modify
        modify()

    elif command == '4':  # command 4
        # view
        view()

    elif command == '5':  # command 5
        # view all
        view_all()

    else:
        # other
        print('# command range in (0-5) ! #')


def main():
    print('Welcome to use this card management system - dirt_version')
    while True:
        # Show prompt message
        show_msg()

        # get input
        user_command = input("Your choose(0-5): ")
        print('=======================')

        # user command
        if user_command == '0':  # command 0
            # quit
            print('# Program End #')
            break

        ch_cmd(user_command)


# save
card_list = []
main()
