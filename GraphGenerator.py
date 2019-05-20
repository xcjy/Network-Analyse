
from __future__ import division
import itertools
import math

import networkx as nx
from networkx.utils import py_random_state
from classic import empty_graph,  complete_graph
#from .degree_seq import degree_sequence_tree
from collections import defaultdict

#__all__是一个字符串list，用来定义模块中对于from XXX import *时要对外导出的符号，
# 即要暴露的借口，但它只对import *起作用，对from XXX import XXX不起作用。

__all__ = [
           'gnp_random_graph',
           'erdos_renyi_graph',
           'watts_strogatz_graph',
           'random_regular_graph',
           'barabasi_albert_graph',
           ]



@py_random_state(2)
def gnp_random_graph(n, p, seed=None, directed=False):
    """Returns a $G_{n,p}$ random graph, also known as an Erdős-Rényi graph
    or a binomial graph.

    The $G_{n,p}$ model chooses each of the possible edges with probability $p$.

    The functions :func:`binomial_graph` and :func:`erdos_renyi_graph` are
    aliases of this function.

    Parameters
    ----------
    n : int
        The number of nodes.
    p : float
        Probability for edge creation.
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.
    directed : bool, optional (default=False)
        If True, this function returns a directed graph.

    See Also
    --------
    fast_gnp_random_graph

    Notes
    -----
    This algorithm [2]_ runs in $O(n^2)$ time.  For sparse graphs (that is, for
    small values of $p$), :func:`fast_gnp_random_graph` is a faster algorithm.

    References
    ----------
    .. [1] P. Erdős and A. Rényi, On Random Graphs, Publ. Math. 6, 290 (1959).
    .. [2] E. N. Gilbert, Random Graphs, Ann. Math. Stat., 30, 1141 (1959).
    """
    if directed:
        edges = itertools.permutations(range(n), 2)
        G = nx.DiGraph()
    else:
        edges = itertools.combinations(range(n), 2)  #方法可以创建一个迭代器，返回iterable中所有长度为r的子序列 即获取全部边
        G = nx.Graph()
    G.add_nodes_from(range(n))  #添加n个节点
    if p <= 0:
        return G
    if p >= 1:
        return complete_graph(n, create_using=G)  #返回完全图

    for e in edges:
        if seed.random() < p:   #概率p添加节点
            G.add_edge(*e)
    return G


# add some aliases to common names

erdos_renyi_graph = gnp_random_graph





@py_random_state(3)
def watts_strogatz_graph(n, k, p, seed=None):

    #参数判断
    if k >= n:
        raise nx.NetworkXError("k>=n, choose smaller k or larger n")

    G = nx.Graph()      #创建图
    nodes = list(range(n))  #  节点标号从0到n-1
    # 构造k-规则图
    # neighbors 连接每一个节点的k/2 个邻居节点
    for j in range(1, k // 2 + 1):
        targets = nodes[j:] + nodes[0:j]  # 构成一个环形数组 如[2,3,4,5,0]
        G.add_edges_from(zip(nodes, targets))  #添加边
    #  重连网络中的每一条边
    #  按照 节点序号及 距离远近 重连 (（即先重连节点序号小的及先重连近的，再重连距离远的）)
    for j in range(1, k // 2 + 1):
        targets = nodes[j:] + nodes[0:j]  # 构成一个环形数组 如[2,3,4,5,0]
        #固定一个节点u 重新挑选另一个节点w
        for u, v in zip(nodes, targets):
            #以概率p重连边。
            if seed.random() < p:
                w = seed.choice(nodes)
                #判断自连与重边的情况
                while w == u or G.has_edge(u, w):
                    w = seed.choice(nodes)
                    #若u节点的度>=n-1 则跳过这次重连
                    if G.degree(u) >= n - 1:
                        break  # skip this rewiring
                else:
                    #删除原来的边，添加新的重连边。
                    G.remove_edge(u, v)
                    G.add_edge(u, w)
    return G


@py_random_state(2)
def random_regular_graph(d, n, seed=None):
    r"""Returns a random $d$-regular graph on $n$ nodes.

    The resulting graph has no self-loops or parallel edges.

    Parameters
    ----------
    d : int
      The degree of each node.
    n : integer
      The number of nodes. The value of $n \times d$ must be even.
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.

    Notes
    -----
    The nodes are numbered from $0$ to $n - 1$.

    Kim and Vu's paper [2]_ shows that this algorithm samples in an
    asymptotically uniform way from the space of random graphs when
    $d = O(n^{1 / 3 - \epsilon})$.

    Raises
    ------

    NetworkXError
        If $n \times d$ is odd or $d$ is greater than or equal to $n$.

    References
    ----------
    .. [1] A. Steger and N. Wormald,
       Generating random regular graphs quickly,
       Probability and Computing 8 (1999), 377-396, 1999.
       http://citeseer.ist.psu.edu/steger99generating.html

    .. [2] Jeong Han Kim and Van H. Vu,
       Generating random regular graphs,
       Proceedings of the thirty-fifth ACM symposium on Theory of computing,
       San Diego, CA, USA, pp 213--222, 2003.
       http://portal.acm.org/citation.cfm?id=780542.780576
    """
    if (n * d) % 2 != 0:
        raise nx.NetworkXError("n * d must be even")

    if not 0 <= d < n:
        raise nx.NetworkXError("the 0 <= d < n inequality must be satisfied")

    if d == 0:
        return empty_graph(n)

    def _suitable(edges, potential_edges):
        # Helper subroutine to check if there are suitable edges remaining
        # If False, the generation of the graph has failed
        if not potential_edges:
            return True
        for s1 in potential_edges:
            for s2 in potential_edges:
                # Two iterators on the same dictionary are guaranteed
                # to visit it in the same order if there are no
                # intervening modifications.
                if s1 == s2:
                    # Only need to consider s1-s2 pair one time
                    break
                if s1 > s2:
                    s1, s2 = s2, s1
                if (s1, s2) not in edges:
                    return True
        return False

    def _try_creation():
        # Attempt to create an edge set

        edges = set()
        stubs = list(range(n)) * d

        while stubs:
            potential_edges = defaultdict(lambda: 0)
            seed.shuffle(stubs)
            stubiter = iter(stubs)
            for s1, s2 in zip(stubiter, stubiter):
                if s1 > s2:
                    s1, s2 = s2, s1
                if s1 != s2 and ((s1, s2) not in edges):
                    edges.add((s1, s2))
                else:
                    potential_edges[s1] += 1
                    potential_edges[s2] += 1

            if not _suitable(edges, potential_edges):
                return None  # failed to find suitable edge set

            stubs = [node for node, potential in potential_edges.items()
                     for _ in range(potential)]
        return edges

    # Even though a suitable edge set exists,
    # the generation of such a set is not guaranteed.
    # Try repeatedly to find one.
    edges = _try_creation()
    while edges is None:
        edges = _try_creation()

    G = nx.Graph()
    G.add_edges_from(edges)

    return G


def _random_subset(seq, m, rng):
    """ Return m unique elements from seq.

    This differs from random.sample which can return repeated
    elements if seq holds repeated elements.

    Note: rng is a random.Random or numpy.random.RandomState instance.
    """
    targets = set()
    while len(targets) < m:
        x = rng.choice(seq)
        targets.add(x)
    return targets


@py_random_state(2)
def barabasi_albert_graph(n, m, seed=None):
   # 参数说明 n为节点个数，m为每步演化加入的边数。

    #参数判断
    if m < 1 or m >= n:
        raise nx.NetworkXError("Barabási–Albert network must have m >= 1"
                               " and m < n, m = %d, n = %d" % (m, n))

    # 生成一个包含m个节点的空图 (即BA模型中t=0时的m0个节点)
    G = empty_graph(m)
    # 初始化目标节点列表，前m个
    targets = list(range(m))
    # 将现有节点按正比于其度的次数加入到一个数组中，初始化时的m个节点度均为0，所以数组为空
    repeated_nodes = []
    #添加其他n-m个节点 第一个下标为m
    source = m
    while source < n:
        # 每次与目标节点 的 加入m条边
        G.add_edges_from(zip([source] * m, targets))
         #加入目标节点到repeated_nodes数组，数组重复次数越多，代表其度越大
        repeated_nodes.extend(targets)
        # 加入源节点m次到repeated_nodes数组，因为源节点的度增加了m。
        repeated_nodes.extend([source] * m)

     #   targets = _random_subset(repeated_nodes, m, seed)
        #重新挑选目标节点
        targets=set()
        # 随机从repeated_nodes数组选择节点， 度越大，重复的次数就越多，选择到的概率就越大，
        # 以此来实现偏好连接。
        #重新挑选m个目标节点
        while len(targets)<m:
            x = seed.choice(repeated_nodes)
            targets.add(x)
        #挑选下一个加入的节点，直到循环的节点数为n为止。
        source += 1
    return G  #返回图


