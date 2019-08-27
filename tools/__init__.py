# # def getMoneyAmount(n):
# # #     """
# # #     C(n); S(n)
# # #     C(a, b) = C(b-a+1)+(a-1)*S(b-a+1)
# # #     """
# # #     cache = [(0, 0), [0, 0], [1, 1], [2, 1]]
# # #     for i in range(len(cache), n+1):
# # #         min_v = n*(n+1)//2
# # #         min_s = 0
# # #         for j in range(1, i+1):
# # #             lv, ls = cache[j-1-1+1]
# # #
# # #             rv, rs = cache[i-j]
# # #             rv += rs*j
# # #
# # #             if lv == rv:
# # #                 vv, ss = lv,  min(rs, ls)
# # #             else:
# # #                 vv, ss = max((lv, ls), (rv, rs))
# # #             vv += j
# # #             if vv < min_v:
# # #                 min_v = vv
# # #                 min_s = ss+1
# # #         cache.append((min_v, min_s))
# # #     return cache[n]
# # # print(getMoneyAmount(20))
# #
# # def getMoneyAmount(n):
# #     """
# #     C(n); S(n)
# #     C(a, b) = C(b-a+1)+(a-1)*S(b-a+1)
# #     """
# #     cache = [(0, []), [0, []], [1, [1]], [2, [2]]]
# #     for i in range(len(cache), n+1):
# #         min_v = n*(n+1)//2
# #         min_s = 0
# #         for j in range(1, i+1):
# #             lv, ls = cache[j-1-1+1]
# #
# #             rv, rs = cache[i-j]
# #
# #             if len(rs) >= 2:
# #                 mid = rs[0]
# #                 rlv, rls = cache[mid-j-1]
# #                 rlv += len(rls)*j
# #                 if rlv > rs[1]:
# #                     continue
# #
# #             rv += len(rs)*j
# #
# #             if lv == rv:
# #                 vv, ss = lv, max(rs, ls, key=len)
# #             else:
# #                 vv, ss = max((lv, ls), (rv, rs))
# #             vv += j
# #             if vv < min_v:
# #                 min_v = vv
# #                 if ss == rs:
# #                     ss = [v+j for v in rs]
# #                 min_s = [j]+ss
# #         cache.append((min_v, min_s))
# #     for i, k in enumerate(cache):
# #         print(i, k[0], k[1:])
# #     return cache[n]
#
# def getMoneyAmount(n):
#     cache = {}
#     def get(a,b):
#         if a>=b:
#             return 0
#         if (a, b) in  cache:
#             return cache[(a,b)]
#         min_v = 10000000
#         for i in range(a, b+1):
#             v = 1 + max(get(a, i-1), get(i+1, b))
#             min_v = min(min_v, v)
#         cache[(a,b)]=min_v
#         return min_v
#     return get(1, n)
# print(getMoneyAmount(10))
# # 38
# import numpy as np
