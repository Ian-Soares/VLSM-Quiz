from random import randint
from time import sleep
import os

def question_maker():
    # RANDOM QUESTIONS MAKER
    randint_classes = randint(0,4)
    if randint_classes == 0:
        random_ip = f'10.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}'
        random_mask = f'{randint(8,30)}'
    elif randint_classes == 1:
        random_ip = f'172.16.{randint(0,255)}.{randint(0,255)}'
        random_mask = f'{randint(16,30)}'
    elif randint_classes == 2:
        random_ip = f'192.168.{randint(0,255)}.{randint(0,255)}'
        random_mask = f'{randint(24,30)}'
    else:
        random_ip = f'{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}'
        random_mask = f'{randint(1,30)}'

    octet_in_list = random_ip.split('.')
    int_octet_in_list = [int(i)for i in octet_in_list]

    binary_mask = str(int(random_mask)*'1')+'0'*(32-int(random_mask))

    ip_in_binary = []
    ip_binary_oct = [bin(i).split('b')[1]for i in int_octet_in_list]

    for i in range(0,len(ip_binary_oct)):
        if len(ip_binary_oct[i]) < 8:
            formatted_binary = ip_binary_oct[i].zfill(8)
            ip_in_binary.append(formatted_binary)
        else:
            ip_in_binary.append(ip_binary_oct[i])

    decimal_mask = f'{int(binary_mask[:8],2)}.{int(binary_mask[8:16],2)}.{int(binary_mask[16:24],2)}.{int(binary_mask[24:],2)}'

    zeros_in_mask = binary_mask.count('0')
    ones_in_mask = 32 - zeros_in_mask

    ip_binary_mask = ''.join(ip_in_binary)

    network_in_binary = ip_binary_mask[:ones_in_mask] + "0" * zeros_in_mask
    broadcast_in_binary = ip_binary_mask[:ones_in_mask] + "1" * zeros_in_mask

    network_oct_bin = []
    broadcast_oct_bin = []

    [network_oct_bin.append(i) for i in [network_in_binary[n:n+8]
    for n in range(0,len(network_in_binary),8)]]
    [broadcast_oct_bin.append(i)for i in [broadcast_in_binary[n:n+8]
    for n in range(0,len(broadcast_in_binary),8)]]
    network_id = '.'.join([str(int(i,2)) for i in network_oct_bin])
    broadcast_ip = '.'.join([str(int(i,2)) for i in broadcast_oct_bin])

    first_host_ip = network_oct_bin[0:3] + [(bin(int(network_oct_bin[3],2)+1).split("b")[1].zfill(8))]
    first_ip = '.'.join([str(int(i,2)) for i in first_host_ip])

    last_host_ip = broadcast_oct_bin[0:3] + [bin(int(broadcast_oct_bin[3],2) - 1).split("b")[1].zfill(8)]
    last_ip = '.'.join([str(int(i,2)) for i in last_host_ip])
    
    # ASKING THE RANDOM QUESTIONS
    while True:
        try:
            print(f'> If the IP Address is {random_ip}/{random_mask}\n'.center(44))
            answer_id = input('The network ID is?(Example: 192.168.1.0): ').strip()
            answer_decmask = input('This mask in decimal is?(Example: 255.255.255.0): ').strip()
            answer_firstip = input('What is the first host of this network?: ').strip()
            answer_lastip = input('The last host?: ').strip()
            answer_broadcast = input('The broadcast?: ').strip()
            break
        except:
            print('Try again, something went wrong.')

    # COMPARING ANSWERS
    right_answr_counter = 0
    if answer_id == network_id:
        print('\nYou got the right network ID, congrats!!!\n')
        sleep(1)
        right_answr_counter += 1
    elif answer_id != network_id:
        print('\nYou failed in the network id, but do not be sad, try to understand where you made the mistake!')
        print(f'The answer was: {network_id}\n')
        sleep(1)

    if answer_decmask == decimal_mask:
        print('\nYou got the right decimal subnet mask, you are doing great!\n')
        sleep(1)
        right_answr_counter += 1
    elif answer_decmask != decimal_mask:
        print('\nYou failed in the decimal mask, but do not be sad, try to understand where you made the mistake!')
        print(f'The answer was: {decimal_mask}\n')
        sleep(1)
    
    if answer_firstip == first_ip:
        print('\nYou got the right first host ip, you are doing fantastic!\n')
        sleep(1)
        right_answr_counter += 1
    elif answer_firstip != first_ip:
        print('\nYou failed in the first host ip, but do not be sad, try to understand where you made the mistake!')
        print(f'The answer was: {first_ip}\n')
        sleep(1)

    if answer_lastip == last_ip:
        print('\nYou got the right last host ip, you are doing amazing!\n')
        sleep(1)
        right_answr_counter += 1
    elif answer_lastip != last_ip:
        print('\nYou failed in the last host ip, but do not be sad, try to understand where you made the mistake!')
        print(f'The answer was: {last_ip}\n')
        sleep(1)

    if answer_broadcast == broadcast_ip:
        print('\nYou got the right broadcast address, you did extremely well!\n')
        sleep(1)
        right_answr_counter += 1
    elif answer_broadcast != broadcast_ip:
        print('\nYou failed in the broadcast address, but do not be sad, try to understand where you made the mistake!')
        print(f'The answer was: {broadcast_ip}\n')
        sleep(1)

    sleep(3)
    try:
        enter_to_continue = input('Press ENTER to continue: ')
    except:
        pass
    if right_answr_counter >= 3:
        return True
    else:
        os.system('cls')
        print('You did not hit 3 right guesses, it will not count as a +1 point.')
        sleep(5)
        return False

score, attempts = 0,0

os.system('cls')
print('='*44)
print('Welcome to the VLSM Quiz'.center(44))
print('Your goal is to score 5 points'.center(44))
print('Good luck'.center(44))
print('='*44)
while True:
    if question_maker():
        score += 1
        attempts += 1
    else:
        attempts += 1   

    if score == 5:
        break
    os.system('cls')
    print(f'Score: {score}')
    print('='*44)
    print('Next question>>>'.center(44))
    print('='*44)

os.system('cls')
print('='*44)
print('You won it, congratulations!!!'.center(44))
print(f'It only took {attempts} attempts.'.center(44))
print('='*44)
sleep(3)
