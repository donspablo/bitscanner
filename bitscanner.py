M = True
N = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
O = print
P = enumerate
Q = divmod
H = len
I = open
J = range
A = str
import os, pickle as E, hashlib as C, binascii as D, multiprocessing as R
from ellipticcurve.privateKey import PrivateKey as V

K = "database/"


def W():
    return D.hexlify(os.urandom(32)).decode("utf-8").upper()


def X(private_key):
    A = V().fromString(bytes.fromhex(private_key))
    return "04" + A.publicKey().toString().hex().upper()


def Y(public_key):
    F = "00"
    A = []
    G = N
    B = C.new("ripemd160")
    I = D.unhexlify(public_key.encode())
    B.update(C.sha256(I).digest())
    K = (F + B.hexdigest()).encode()
    L = C.sha256(D.unhexlify(K)).digest()
    H = F + B.hexdigest() + C.sha256(L).hexdigest()[0:8]
    O = [A != "0" for A in H].index(M) // 2
    E = int(H, 16)
    while E > 0:
        E, P = Q(E, 58)
        A.append(G[P])
    for R in J(O):
        A.append(G[0])
    return "".join(A[::-1])


def Z(private_key, public_key, address, database):
    F = "\n"
    G = "Wallet Address: "
    H = "a"
    J = public_key
    C = database
    D = private_key
    B = address
    if B in C[0] or B in C[1] or B in C[2] or B in C[3]:
        with I("success.txt", H) as E:
            E.write(
                A(G) + A(F)
                + A(B) + A(F)
                + "Public Key: "
                + A(J) + A(F)
                + "Private Key (Hex): "
                + A(D) + A(F)
                + "Private Key (WIF): "
                + A(S(D))
                + A(F) + A(F)
            )
    else:
        with I("failed.txt", H) as E:
            E.write(            
                A(G) + A(F)
                + A(B) + A(F)
                + "Public key: "
                + A(J) + A(F)
                + "Private Key (Hex): "
                + A(D) + A(F)
                + "Private Key (WIF): "
                + A(S(D))
                + A(F) + A(F)
            )


def S(private_key):
    I = "80"
    J = private_key
    M = C.sha256(D.unhexlify(I + J)).hexdigest()
    E = C.sha256(D.unhexlify(M)).hexdigest()
    E = D.unhexlify(I + J + E[0:8])
    K = F = N
    A = L = 0
    B = ""
    for (O, G) in P(E[::-1]):
        A += 256 ** O * G
    while A >= H(K):
        R, S = Q(A, H(K))
        B, A = F[S] + B, R
    B = F[A] + B
    for G in E:
        if G == 0:
            L += 1
        else:
            break
    return F[0] * L + B


def a(database):
    while M:
        A = W()
        B = X(A)
        C = Y(B)
        Z(A, B, C, database)


if __name__ == "__main__":
    B = [set() for A in J(4)]
    T = H(os.listdir(K))
    L = T // 2
    U = L // 2
    for (F, b) in P(os.listdir(K)):
        O("\rscanning bitcoin database(s): " + A(F + 1) + "/" + A(T), end=" ")
        with I(K + b, "rb") as G:
            if F < L:
                if F < U:
                    B[0] = B[0] | E.load(G)
                else:
                    B[1] = B[1] | E.load(G)
            elif F < L + U:
                B[2] = B[2] | E.load(G)
            else:
                B[3] = B[3] | E.load(G)
    O("Scan Completed, Bitscanner initialized!")
    for c in J(R.cpu_count()):
        R.Process(target=a, args=(B,)).start()
