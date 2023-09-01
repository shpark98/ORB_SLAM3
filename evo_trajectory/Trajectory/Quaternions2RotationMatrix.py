import os
import numpy as np


def quaternion_to_rotation_matrix(q):
    w, x, y, z = q

    rotation_matrix = np.array(
        [
            [1 - 2 * y * y - 2 * z * z, 2 * x * y - 2 * w * z, 2 * x * z + 2 * w * y],
            [2 * x * y + 2 * w * z, 1 - 2 * x * x - 2 * z * z, 2 * y * z - 2 * w * x],
            [2 * x * z - 2 * w * y, 2 * y * z + 2 * w * x, 1 - 2 * x * x - 2 * y * y],
        ]
    )

    return rotation_matrix


if __name__ == "__main__":
    input_file_path = "./KITTI_00_ORB_MONO.txt"
    output_file_path = "./KITTI_00_ORB_MONO_Q2R.txt"

    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    with open(input_file_path, "r") as input_file, open(
        output_file_path, "w"
    ) as output_file:
        for line in input_file:
            d = line.split(" ")
            x = float(d[1])
            y = float(d[2])
            z = float(d[3])
            q_w = float(d[4])
            q_i = float(d[5])
            q_j = float(d[6])
            q_k = float(d[7])
            r = quaternion_to_rotation_matrix(np.array([q_w, q_i, q_j, q_k]))
            r = r.reshape(1, 9)[0]
            new_line = "{} {} {} {} {} {} {} {} {} {} {} {}\n".format(
                r[0], r[1], r[2], x, r[3], r[4], r[5], y, r[6], r[7], r[8], z
            )
            output_file.write(new_line)