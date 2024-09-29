install(FILES "opencv2/opencv.hpp"
    DESTINATION ${/Users/amakki/Documents/Coding-Design/GitHub/empty for Github clones/Maksportfolio/MaksPortfolio/Main.py}/opencv2
    COMPONENT dev)
cv2::Mat image;
// Load an image from file
image = cv2::imread("/path/to/your/image.jpg", cv2::IMREAD_COLOR);

if (!image.data) {
    std::cout << "Error: Could not open or find the image." << std::endl;
    return -1;
}

// Display the image
cv2::namedWindow("Display window", cv2::WINDOW_AUTOSIZE);
cv2::imshow("Display window", image);

// Wait for a key press
cv2::waitKey(0);

// Release resources
cv2::destroyAllWindows();