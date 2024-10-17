def correct_rounding(number):
    if number > 0:
        return int(number + 0.5)
    else:
        return int(number + -0.5)

n = int(input())
if n == 0:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    l = [input().split(":") for i in range(n)]
    _yes, _no = 0, 0
    _users = set()


    for i in l:
        if i[1] == " Correct":
            _yes += 1
            _users.add(i[0])
        else: _no += 1

    _total = _yes + _no
    _proc_yes = correct_rounding(_yes * 100 / _total)

    if _total == _no:
        print("Вы можете стать первым, кто решит эту задачу")
    else:
        print(f"Верно решили {len(_users)} учащихся")
        print(f"Из всех попыток {_proc_yes}% верных")