class Transaction:
    def __init__(self):
        self.items = {}
        self.total_price = 0

    def add_item(self, nama, jumlah, harga):
        self.items[nama] = {'jumlah': jumlah,
                            'harga': harga, 'total harga': jumlah*harga}

    def check_out(self):
        for i in self.items.keys():
            harga = 0
            if self.items[i]['total harga'] > 500_000:
                diskon = self.items[i]['total harga'] * 0.07
            elif self.items[i]['total harga'] > 300_000:
                diskon = self.items[i]['total harga'] * 0.06
            elif self.items[i]['total harga'] > 200_000:
                diskon = self.items[i]['total harga'] * 0.05
            else:
                diskon = 0

            harga += (self.items[i]['total harga'] - diskon)
            print(harga)
            self.total_price += harga

        print(int(self.total_price))

    def update_item_name(self, lama, baru):
        try:
            self.items[baru] = self.items.pop(lama)
        except KeyError:
            print('nama barang tidak ditemukan')

    def update_item_qty(self, nama, jumlah):
        try:
            self.items[nama]['jumlah'] = jumlah
        except KeyError:
            print('nama barang tidak ditemukan')

    def update_item_price(self, nama, harga):
        self.items[nama]['harga'] = harga

    def delete_item(self, nama):
        del self.items[nama]

    def reset_transaction(self):
        self.items = {}
        print('Semua item berhasil dihapus')


a = Transaction()
a.add_item('anggur', 100, 6000)
a.add_item('jeruk', 5, 3000)
print(a.items)
a.check_out()
a.update_item_name('jeruk', 'Jeruk')
print(a.items)
a.update_item_qty('anggur', 50)
print(a.items)
a.update_item_price('anggur', 4000)
print(a.items)
a.delete_item('anggur')
print(a.items)
a.check_out()
a.reset_transaction()
print(a.items)
