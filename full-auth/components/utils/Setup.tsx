"use client";

import { useVerifyMutation } from "@/redux/features/authApiSlice";
import { finishInitialLoad, setAuth } from "@/redux/features/authSlice";
import { useAppDispatch } from "@/redux/hooks";
import { useEffect } from "react";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export default function Setup() {
  const [verify] = useVerifyMutation();
  const dispatch = useAppDispatch();

  useEffect(() => {
    verify(undefined)
      .unwrap()
      .then(() => {
        dispatch(setAuth());
      })

      .finally(() => {
        dispatch(finishInitialLoad());
      });
  }, []);

  return <ToastContainer />;
}
