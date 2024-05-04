import { useState, ChangeEvent, FormEvent } from "react";
import { toast } from "react-toastify";
import { useRouter } from "next/navigation";
import { useLoginMutation } from "@/redux/features/authApiSlice";
import { setAuth } from "@/redux/features/authSlice";
import { useAppDispatch } from "@/redux/hooks";

export default function useLogin() {
  const router = useRouter();
  const dispatch = useAppDispatch();
  const [login, { isLoading }] = useLoginMutation();
  
  const [formData, setFormData] = useState({
      email: "",
      password: "",
    });
  
  const {  email, password } = formData;
  const onChange = (event: ChangeEvent<HTMLInputElement>) => {
      const { name, value } = event.target;
      setFormData({ ...formData, [name]: value });
    };
  
  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
      event.preventDefault();
      login({ email, password })
        .unwrap()
        .then(() => {
          dispatch(setAuth())
          toast.success("Logged in");
          router.push("/dashboard");
        })
        .catch((error) => {

          toast.error('Failed to log in'); 
        });
    };

  return {
     email,
        password,
        isLoading,
        onChange,
        onSubmit,
    }
}