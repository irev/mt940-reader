# mt940-reader
tool reading file mt940
```
pip instal -r requirements.txt
```

python .\mt940-reader.py {dir}
```
python .\mt940-reader.py D:\MT940\\BMRI\Juli\
```
------------------

MT940 File


------------------

MT940 adalah file format swift yang menampilkan transaksi yang terjadi.

Dari BRI akan menyediakan file MT940 melalui dua metode:

1.  SFTP (partner akan diberikan username dan password untuk akses file SFTP)
2.  Dikirim via Email

Setiap file MT940 merepresentasikan seluruh transaksi yang terjadi H-1. Untuk mendapatkan file MT940 ini, silahkan kontak ke tim BRIAPI untuk penjelasan lebih detail.

Penamaan File MT940 menggunakan format berikut  `"042801020365703.202107140256 042801020365703 -> Nomor rekening 20210714 -> Tanggal transaksi H-1 0256 -> Waktu generate ke SFTP"`

**Sample File:**

               
            {1:BRI}{2:940SI}{4:
            :20:20161116022517
            :25:042801020365703
            :28C:321
            :60F:C161116IDR1100000
            :61:161116D1469582861NTRF
            :86:GFV844469 0749 TJBB 16112016
            :62F:C161116IDR1100000
            -}
        

Component

Mandatory

Deskripsi

Contoh

Statement Date

M

Date mt940 was generated

`:20:20161116022517`

*   20161116022517 follow the format YYYYMMDDHHMMSS

Account Number

M

Account Number, 15 numeric characters

`:25:042801020365703`

*   042801020365703 → account number

Sequence

M

Statement number / sequence number, 3 numeric characters

`:28C:226`

*   226 → sequence number

Opening Balance

M

Starting Balance, consisting of:

*   Debit / credit balance status
*   Date
*   Currency
*   Total of balance (position)

`:60F:C161116IDR1100000`

*   C → debit/credit balance status (D/C)
*   161116 → 6 numeric characters format YYMMDD
*   IDR → 3 currency characters
*   1100000 → balance, numeric

Statement Line

M

Statement Line, consisting of:

*   Date
*   Debit/credit balance status
*   Nominal
*   Transaction code identification

`:61:161116D1469582861NTRF`

*   161116 → 6 numeric characters format YYMMDD
*   D → debet / kredit (D/C)
*   1469582861 → nominal
*   TRF → transaction code (please see the list of transaction codes below)

Information Account / Header

O

description, a maximum length of 40 characters

`:86:GFV844469 0749 TJBB 16112016`

*   GFV844469 0749 TJBB 16112016 → description/remark

Account Header

M

Final Balance, consisting of:

*   Debit/credit balance status
*   Date
*   Currency
*   Total balance (position)

`:62F:C161116IDR1100000`

*   C → Status saldo debet/kredit (D/C)
*   161116 → 6 numeric characters format YYMMDD
*   IDR → 3 currency characters
*   1100000 → saldo, numerik

> Seluruh response error yang tidak tercantum dalam list response BRIAPI memiliki status **pending** dan perlu dilakukan pengecekan

## 

Transaction Code Description

| TRX Type | Deskripsi |
| --- | --- |
| NCHG | MACAM-MACAM BIAYA |
| NCHG | CA MISC CHARGES |
| NCHG | BIAYA ADMINISTRASI |
| NCHG | CA BILL PAYMENT |
| NCHG | BIAYA TRANSFER OTOMATIS |
| NCHG | BIAYA BULANAN ATM |
| NCHG | PAYMENT CA GL |
| NCHG | BIAYA,ADMINISTRASI |
| NCHG | BIAYA TRANSAKSI ATM |
| NCHG | KOREKSI BUNGA KE SALDO |
| NCMI | PENARIKAN,TUNAI |
| NCMI | SETORAN,TUNAI |
| NIND | PEMBAYARAN,BUNGA,DEPOSITO |
| NINT | BUNGA,REKENING |
| NINT | KOREKSI BUNGA KE SALDO |
| NINT | PEMBAYARAN BUNGA DEPOSITO |
| NINT | TD INT PAY CA |
| NINT | PENYESUAIAN BUNGA |
| NINT | TRANSFER BUNGA |
| NINT | BUNGA REKENING |
| NINT | KOREKSI BUNGA KRN VALUTA MUNDUR |
| NMSC | BF-COMPRESSED ITEMS DEBIT |
| NMSC | PAJAK |
| NMSC | MISCELLANEOUS |
| NMSC | BF-COMPRESSED ITEMS CREDIT |
| NTAX | PAJAK |
| NTDD | PENEMPATAN,DEPOSITO |
| NTDW | PENCAIRAN,DEPOSITO |
| NTRE | TRANSFER MASUK |
| NTRF | INW DR RTGS CA |
| NTRF | OB CA SA |
| NTRF | TD WITHDRAW O/B CA |
| NTRF | TC CEP SALES OVB CA |
| NTRF | TC CEP PURCH OVB CA |
| NTRF | CD WITHDRAW O/B CA |
| NTRF | PAYMENT RTGS |
| NTRF | LN SETLEMENT CA |
| NTRF | PAYMENT SKN |
| NTRF | LN DR ADJ PRINC-CA |
| NTRF | INCENTIVE PAID FROM LOAN |
| NTRF | PEMBAYARAN OB GIRO |
| NTRF | LN REP MN SPL OVB CA |
| NTRF | SA OVERBOOKING CA |
| NTRF | RM TRF CA TO CA |
| NTRF | TT ISS OVB CA OUT |
| NTRF | RM BTOB OVB CA |
| NTRF | RTGS RPUR OVB CA |
| NTRF | INW RTGS TRF OVB CA |
| NTRF | RM TRF CA TO CASH |
| NTRF | RM TRF CA TO SA |
| NTRF | CD PLACEMENT O/B CA |
| NTRF | WESEL PAY OVB CA |
| NTRF | PENUTUPAN REK TUNAI |
| NTRF | RM BTOB PAY OVB CA |
| NTRF | BILL PAYMENT KREDIT |
| NTRF | WESEL ISS OVB CA |
| NTRF | LN CR ADJ PRINC-CA |
| NTRF | PRK OVERBOOKING CA |
| NTRF | PENARIKAN TUNAI |
| NTRF | OB CA CA |
| NTRF | PEMINDAHBUKUAN |
| NTRF | CA CHEQUE RETURN |
| NTRF | CA/PRK INW CLEARING |
| NTRF | RM TRF CASH TO CA |
| NTRF | LN CAP REPY OVB CA |
| NTRF | LOCAL CHEQUE CREDIT |
| NTRF | LN REP MNL OB CA REV |
| NTRF | TRANSFER,MASUK |
| NTRF | LN DISBUR OVB CA |
| NTRF | RTGS TRF OVB CA |
| NTRF | PEMBAYARAN TUNAI |
| NTRF | TRANSFER,KELUAR |
| NTRF | TT PAY OVB CA IN |
| NTRF | PENUTUPAN REK OB |
| NTRF | LN DR ADV PYMNT-CA |
| NTRF | CN TRANSFER OVB CA |
| NTRF | PEMBAYARAN OB TABUNGAN |
| NTRF | DR SIDE OF SALARY CREDITING |
| NTRF | CA DEBIT GL CREDIT |
| NTRF | LN DISBUR OVB CA RV |
| NTRF | LN SETLL CA REV |
| NTRF | LN INST RPY OVB CA |
| NTRF | TD PLACEMENT O/B CA |
| NTRF | TC PURCH OVB CA |
| NTRF | TRANSFER OTOMATIS |
| NTRF | CN CANCELATION CA |
| NTRF | INW CA TRF TO CA |
| NTRF | BILL PAYMENT DEBIT |
| NTRF | SETORAN TUNAI |
| NTRF | CA CLOSE ACC OVB CA |
| NTRF | CR SIDE OF SALARY CREDITING |
| NTRF | CA CASH WITHDRAWAL |
| NTRF | INWARD RTGS CR |
| NTRF | CA CASH DEPOSIT |
| NTRF | TC SALES OVB CA |
| NTRF | CA OVERBOOKING CA |
| NTRF | CA OVERBOOKING SA |
