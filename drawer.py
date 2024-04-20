import cv2
class drawer:
    def __init__(self):
        pass

    def rounded_rectangle(self, src, topLeft, bottomRight, lineColor, thickness, cornerRadius):
        # corners:
        # p1 - p2
        # |     |
        # p4 - p3

        p1 = topLeft
        p2 = (bottomRight[0], topLeft[1])
        p3 = bottomRight
        p4 = (topLeft[0], bottomRight[1])

        # draw straight lines
        cv2.line(src, (p1[0] + cornerRadius, p1[1]), (p2[0] - cornerRadius, p2[1]), lineColor, thickness)
        cv2.line(src, (p2[0], p2[1] + cornerRadius), (p3[0], p3[1] - cornerRadius), lineColor, thickness)
        cv2.line(src, (p4[0] + cornerRadius, p4[1]), (p3[0] - cornerRadius, p3[1]), lineColor, thickness)
        cv2.line(src, (p1[0], p1[1] + cornerRadius), (p4[0], p4[1] - cornerRadius), lineColor, thickness)

        # draw arcs
        cv2.ellipse(src, (p1[0] + cornerRadius, p1[1] + cornerRadius), (cornerRadius, cornerRadius), 180.0, 0, 90,
                    lineColor, thickness)
        cv2.ellipse(src, (p2[0] - cornerRadius, p2[1] + cornerRadius), (cornerRadius, cornerRadius), 270.0, 0, 90,
                    lineColor, thickness)
        cv2.ellipse(src, (p3[0] - cornerRadius, p3[1] - cornerRadius), (cornerRadius, cornerRadius), 0.0, 0, 90,
                    lineColor, thickness)
        cv2.ellipse(src, (p4[0] + cornerRadius, p4[1] - cornerRadius), (cornerRadius, cornerRadius), 90.0, 0, 90,
                    lineColor, thickness)

        return src
