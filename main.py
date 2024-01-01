import networkx as nx
# kiểm tra 2 đồ thị có đẳng cấu hay không
def is_subgraph_isomorphic(adj_matrix_G, adj_matrix_H):
    # Tạo đồ thị từ ma trận kề
    G = nx.Graph(adj_matrix_G)
    H = nx.Graph(adj_matrix_H)

    # Kiểm tra đồ thị con đẳng cấu
    return nx.is_isomorphic(G, H)

# tạo đồ thị thích hợp cho hàm từ dữ liệu của input dataset
def create_graph_from_file(filename):
    graph = nx.Graph()
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                u = int(parts[0])
                v = int(parts[1])
                graph.add_edge(u, v)  # Chỉ lấy u và v, bỏ qua weight
    return graph
#========================== Đọc file _adj.tsv ==========================#

tsvfile='test_adj.tsv' #lấy đường dẫn vào tsvfile
graph1 = create_graph_from_file(tsvfile) #tạo đồ thị H
    
#========================== End Đọc file _adj.tsv ==========================#


#========================== Đọc file _inc.tsv ==========================#

tsvfile='test_inc.tsv' #lấy đường dẫn vào tsvfile
graph2 = create_graph_from_file(tsvfile) #tạo đồ thị G

#========================== End Đọc file _inc.tsv ==========================#

# Xác định xem H có phải là đồ thị con đẳng cấu của G hay không
result = is_subgraph_isomorphic(graph1, graph2)
print(result)
