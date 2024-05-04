import { useState, ChangeEvent, FormEvent } from "react";
import { toast } from "react-toastify";
import { useRouter } from "next/navigation";
import { useRegisterMutation } from "@/redux/features/authApiSlice";

export default function useRegister() {
    const router = useRouter();
    const [register, { isLoading }] = useRegisterMutation();
  
    const [formData, setFormData] = useState({
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      re_password: "",
    });
  
    const { first_name, last_name, email, password, re_password } = formData;
    const onChange = (event: ChangeEvent<HTMLInputElement>) => {
      const { name, value } = event.target;
      setFormData({ ...formData, [name]: value });
    };
  
    const onSubmit = (event: FormEvent<HTMLFormElement>) => {
      event.preventDefault();
      register({ first_name, last_name, email, password, re_password })
        .unwrap()
        .then(() => {
          toast.success("Please check email to verify account");
          router.push("/auth/login");
        })
        .catch((error) => {
          // console.error("Error:", error);

          // Extract the error message from the error object
          const errorMessage = error.data.email[0]; // Assuming the error message is the first element of the email array
    
          toast.error(errorMessage); // Display the error message to the user
        });
    };

    return {
        first_name,
        last_name, email,
        password,
        re_password,
        isLoading,
        onChange,
        onSubmit,
    }
}