import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10, 2),
                           index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7],
                           columns=['col2', 'col1'])
print(unsorted_df, '->unsorted_df')

# 按标签进行排序
# 使用sort_index()方法, 通过传递axis参数和排序顺序, 可以对DataFrame进行排序.
# 默认情况下, 按照升序对行标签进行排序
sorted_df = unsorted_df.sort_index()        # 参数axis=1可对列进行排序, ascending=False控制升降序
print(sorted_df, '->sorted')

# 按某列值进行排序
# sort_values(by=['col']
sorted_df = unsorted_df.sort_values(by='col1', ascending=False)
print(sorted_df)
# 先按col1排, 再按col2排
sorted_df = unsorted_df.sort_values(by=['col1', 'col2'], ascending=[True, False])
print(sorted_df)
