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
      console.log("submit hit");
      event.preventDefault();
      register({ first_name, last_name, email, password, re_password })
        .unwrap()
        .then(() => {
          toast.success("Please check email to verify account");
          router.push("/auth/login");
        })
        .catch(() => {
          toast.error("Failed to register account");
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