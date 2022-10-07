
import pickle as u, os, random as a, time, os, hashlib as C, binascii as P, codecs as B, ecdsa as f, time, multiprocessing as b
from pymemcache.client import base as Q
from datetime import datetime as F

S = "r"
T = "test.txt"
U = "localhost"
V = "%m/%d/%Y, %H:%M:%S"
W = True
X = dict
Y = round
e = enumerate
Z = len
N = ""
O = " "
J = open
G = str
A = print
c = b"get_misses"
d = b"reclaimed"
g = b"evictions"
h = O
i = W
j = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
k = J
l = range
R = V
K = N
L = int
H = Z
E = G
D = A
m = Q.Client((U, 11211))
n = L(b.cpu_count() / 2)
o = 32
z = K
A0 = K
p = "3PQtD6B1crUVvNHt6fVY5HvdajRrJ6EeGq"
q = "1Ca72914TemMMuDpAscEMeZV3494sztc81"
r = U
M = V
I = "\n"


def s(address_hex):
    B = address_hex
    D = j
    A = K
    E = H(B) - H(B.lstrip("0"))
    C = L(B, 16)
    while C > 0:
        F = C % 58
        G = D[F]
        A = G + A
        C //= 58
    I = E // 2
    for J in l(I):
        A = "1" + A
    return A


def v(num_keys):
    g = b"00"
    h = "ripemd160"
    M = "utf-8"
    A = "hex"
    i = []
    for k in l(num_keys):
        I = os.urandom(32).hex()
        m = f.SigningKey.from_string(
            B.decode(I, A), curve=f.SECP256k1
        ).verifying_key.to_string()
        n = b"04" + B.encode(m, A)
        q = B.decode(n, A)
        N = C.sha256(q)
        O = N.digest()
        D = C.new(h)
        D.update(O)
        Q = D.digest()
        R = B.encode(Q, A)
        S = g
        E = S + R
        T = B.decode(E, A)
        U = C.sha256(T)
        V = U.digest()
        W = C.sha256(V)
        X = W.digest()
        Y = B.encode(X, A)
        Z = Y[:8]
        a = (E + Z).decode(M)
        r = s(a)
        b = B.encode(m, A)
        t = b.decode(M)
        u = H(b) // 2
        v = b[:u]
        w = L(t[-1], 16)
        x = b"02" if w % 2 == 0 else b"03"
        y = x + v
        z = B.decode(y, A)
        N = C.sha256(z)
        O = N.digest()
        D = C.new(h)
        D.update(O)
        Q = D.digest()
        R = B.encode(Q, A)
        S = g
        E = S + R
        T = B.decode(E, A)
        U = C.sha256(T)
        V = U.digest()
        W = C.sha256(V)
        X = W.digest()
        Y = B.encode(X, A)
        Z = Y[:8]
        a = (E + Z).decode(M)
        A0 = s(a)
        A1 = C.sha256(P.unhexlify("80" + I)).hexdigest()
        J = C.sha256(P.unhexlify(A1)).hexdigest()
        J = P.unhexlify("80" + I + J[0:8])
        o = c = j
        F = p = 0
        G = K
        for (k, d) in e(J[::-1]):
            F += 256 ** k * d
        while F >= H(o):
            A2, A3 = divmod(F, H(o))
            G, F = c[A3] + G, A2
        G = c[F] + G
        for d in J:
            if d == 0:
                p += 1
            else:
                break
        A4 = c[0] * p + G
        i.append([I, A4, n, r, A0])
    return i


def w(keys_list):
    A = keys_list
    B = []
    for C in A:
        B.append(C[3])
        B.append(C[4])
    G = m.get_multi(B)
    if G:
        D(G)
        D(A)
        with k("found.txt", "a") as H:
            for C in A:
                H.write(E(G))
                H.write(E(A))
        D(F.now().strftime(R))
        D("GOT ONE")


def x(test_1_s, test_2_s):
    B = L(100000 / o - 1)
    A = B + 1
    while i:
        C = v(o)
        w(C)
        A = A + 1


def y():
    D("available threads: " + E(n))
    B = 0
    C = k(T, S)
    G = C.readline().strip()
    H = C.readline().strip()
    C.close()
    D("sanities: " + G + h + H)
    D(F.now().strftime(R))
    while B < n:
        D("thread spawned: " + E(B))
        B = B + 1
        b.Process(target=x, args=(G, H)).start()
    while i:
        time.sleep(15)
        A = m.stats()
        D(
            "\r "
            + F.now().strftime(R)
            + "  evictions: "
            + E(A.get(g))
            + " reclaimed: "
            + E(A.get(d))
            + " Connections: "
            + E(A.get(b"curr_connections"))
            + " Misses: "
            + E(A.get(c))
            + " MPS: "
            + E(Y(A.get(c) / A.get(b"uptime"), 2)),
            end=h,
        )
        if A.get(g) > 0 or A.get(d) > 0:
            D("!!! ERRORR !!!")


def t():
    C = "data/"
    A("loading memcached...")
    D = Q.Client((r, 11211))
    A("uploading data...")
    A(F.now().strftime(M))
    b = Z(os.listdir(C))
    H = D.get_multi([q, p])
    if H:
        A("test check pass")
    else:
        for (c, d) in e(os.listdir(C)):
            A("\rreading data: " + G(c + 1) + "/" + G(b), end=O)
            with J(C + d, "rb") as f:
                R = u.load(f)
                D.set_multi(X.fromkeys(R, 1), expire=0)
            R = []
        A("data loaded!")
        A(F.now().strftime(M))
        H = D.get_multi([p, q])
        if H:
            A("testing passed!")
        else:
            A("testing failed!")
    C = "data/data.txt"
    g = a.randint(0, 34000000)
    h = a.randint(0, 34000000)
    K = N
    L = N
    A("connect memcached...")
    D = Q.Client((r, 11211))
    A("Loading and injecting data")
    A(F.now().strftime(M))
    i = time.time()
    E = 0
    B = J(C, S)
    while W:
        U = []
        V = B.readlines(32768)
        if not V:
            break
        for P in V:
            U.append(P.rstrip(I))
            E += 1
            if E == g:
                K = P.rstrip(I)
            if E == h:
                L = P.rstrip(I)
        D.set_multi(X.fromkeys(U, 1), expire=0)
        A("\raddresses: " + G(E), end=O)
    B.close()
    j = time.time()
    k = j - i
    A("DATA LOADED: Addresses loadeded in " + G(Y(k, 2)) + " seconds!")
    A("test 1: " + K + " test 2: " + L)
    A(F.now().strftime(M))
    B = J(T, "w")
    B.write(K + I)
    B.write(L + I)
    B.close()
    y()


if __name__ == "__main__":
    try:
        t()
    except:
        t()
