import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const DangXuat = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const logout = async () => {
      try {
        // Retrieve the tokens from localStorage
        const accessToken = localStorage.getItem("access_token");
        const refreshToken = localStorage.getItem("refresh_token");

        if (!accessToken || !refreshToken) {
          throw new Error("Token không tồn tại.");
        }

        // Send the logout request using axios
        const response = await axios.post(
          "http://127.0.0.1:8888/api/manager/logout/",
          { refresh_token: refreshToken },
          {
            headers: {
              Authorization: `Bearer ${accessToken}`, // Send the access token
              "Content-Type": "application/json",
            },
            withCredentials: true, // Ensure cookies are sent with the request
          }
        );

        if (response.status !== 200) {
          throw new Error("Đăng xuất thất bại.");
        }

        // Clear tokens from localStorage
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");

        // Navigate to the homepage and reload the page
        navigate("/");
        window.location.reload();
      } catch (err) {
        console.error("Đăng xuất lỗi:", err.message || "Đã xảy ra lỗi không xác định");
      }
    };

    logout(); // Call the logout function when the component renders
  }, [navigate]); // Add navigate as a dependency to avoid ESLint warning

  return null; // Nothing is rendered in this component
};

export default DangXuat;
