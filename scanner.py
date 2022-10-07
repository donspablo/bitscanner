P = b"get_misses"
Q = b"reclaimed"
R = b"evictions"
S = " "
T = True
e = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
U = open
f = range
H = "%m/%d/%Y, %H:%M:%S"
I = ""
J = int
F = len
D = str
B = print
import os, hashlib as C, binascii as M, codecs as A, ecdsa as g, time, multiprocessing as V
from datetime import datetime as K
from pymemcache.client import base

W = base.Client(("localhost", 11211))
X = J(V.cpu_count() / 2)
Y = 32
L = I
N = I


def h(address_hex):
    B = address_hex
    D = e
    A = I
    E = F(B) - F(B.lstrip("0"))
    C = J(B, 16)
    while C > 0:
        G = C % 58
        H = D[G]
        A = H + A
        C //= 58
    K = E // 2
    for L in f(K):
        A = "1" + A
    return A


def Z(num_keys):
    i = b"00"
    j = "ripemd160"
    N = "utf-8"
    B = "hex"
    k = []
    for l in f(num_keys):
        K = os.urandom(32).hex()
        m = g.SigningKey.from_string(
            A.decode(K, B), curve=g.SECP256k1
        ).verifying_key.to_string()
        n = b"04" + A.encode(m, B)
        q = A.decode(n, B)
        O = C.sha256(q)
        P = O.digest()
        D = C.new(j)
        D.update(P)
        Q = D.digest()
        R = A.encode(Q, B)
        S = i
        E = S + R
        T = A.decode(E, B)
        U = C.sha256(T)
        V = U.digest()
        W = C.sha256(V)
        X = W.digest()
        Y = A.encode(X, B)
        Z = Y[:8]
        a = (E + Z).decode(N)
        r = h(a)
        b = A.encode(m, B)
        s = b.decode(N)
        t = F(b) // 2
        u = b[:t]
        v = J(s[-1], 16)
        w = b"02" if v % 2 == 0 else b"03"
        x = w + u
        y = A.decode(x, B)
        O = C.sha256(y)
        P = O.digest()
        D = C.new(j)
        D.update(P)
        Q = D.digest()
        R = A.encode(Q, B)
        S = i
        E = S + R
        T = A.decode(E, B)
        U = C.sha256(T)
        V = U.digest()
        W = C.sha256(V)
        X = W.digest()
        Y = A.encode(X, B)
        Z = Y[:8]
        a = (E + Z).decode(N)
        z = h(a)
        A0 = C.sha256(M.unhexlify("80" + K)).hexdigest()
        L = C.sha256(M.unhexlify(A0)).hexdigest()
        L = M.unhexlify("80" + K + L[0:8])
        o = c = e
        G = p = 0
        H = I
        for (l, d) in enumerate(L[::-1]):
            G += 256 ** l * d
        while G >= F(o):
            A1, A2 = divmod(G, F(o))
            H, G = c[A2] + H, A1
        H = c[G] + H
        for d in L:
            if d == 0:
                p += 1
            else:
                break
        A3 = c[0] * p + H
        k.append([K, A3, n, r, z])
    return k


def a(keys_list):
    A = keys_list
    C = []
    for E in A:
        C.append(E[3])
        C.append(E[4])
    F = W.get_multi(C)
    if F:
        B(F)
        B(A)
        with U("found.txt", "a") as G:
            for E in A:
                G.write(D(F))
                G.write(D(A))
        B(K.now().strftime(H))
        B("GOT ONE")


def b(test_1_s, test_2_s):
    B = J(100000 / Y - 1)
    A = B + 1
    while T:
        C = Z(Y)
        a(C)
        A = A + 1


if __name__ == "__main__":
    B("available threads: " + D(X))
    G = 0
    O = U("test.txt", "r")
    L = O.readline().strip()
    N = O.readline().strip()
    O.close()
    B("sanities: " + L + S + N)
    B(K.now().strftime(H))
    while G < X:
        B("thread spawned: " + D(G))
        G = G + 1
        V.Process(target=b, args=(L, N)).start()
    while T:
        time.sleep(15)
        E = W.stats()
        B(
            "\r "
            + K.now().strftime(H)
            + "  evictions: "
            + D(E.get(R))
            + " reclaimed: "
            + D(E.get(Q))
            + " Connections: "
            + D(E.get(b"curr_connections"))
            + " Misses: "
            + D(E.get(P))
            + " MPS: "
            + D(round(E.get(P) / E.get(b"uptime"), 2)),
            end=S,
        )
        if E.get(R) > 0 or E.get(Q) > 0:
            B("!!! ERRORR !!!")
