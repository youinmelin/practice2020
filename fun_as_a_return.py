def get_sum(m):
    def sum(n):
        return m + n
    return sum

fn100 = get_sum(100)
fn1000 = get_sum(1000)
print(fn100(5))
print(fn1000(5))

