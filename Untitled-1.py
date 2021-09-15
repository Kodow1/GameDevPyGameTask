for cell in cell_list:
        if cell.y != 0: #not at the top
            print(cell.name,"-10")
            cell.adjacent["up"] = int(cell.name)-10
            cell.shared_walls.append("up")
        if cell.y != height-1: #not at bottom
            print(cell.name,"+10")
            cell.adjacent["down"] = int(cell.name)+10
            cell.shared_walls.append("down")
        if cell.x != 0: #not far left
            print(cell.name,"-1")
            cell.adjacent["left"]= int(cell.name)-1
            cell.shared_walls.append("left")
        if cell.x != width-1: #not far right
            cell.adjacent["right"]= int(cell.name)+1
            cell.shared_walls.append("right")

        







