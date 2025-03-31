import { forwardRef } from "react";

interface Props {
  message: string;
}

const Toast = forwardRef<HTMLDivElement, Props>(({ message }, ref) => (
  <div className="position-fixed bottom-0 end-0 p-3" style={{ zIndex: 9999 }}>
    <div
      ref={ref}
      className="toast align-items-center text-bg-success border-0"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
      
    >
      <div className="d-flex">
        <div className="toast-body">{message}</div>
        <button
          type="button"
          className="btn-close btn-close-white me-2 m-auto"
          data-bs-dismiss="toast"
          aria-label="Close"
        ></button>
      </div>
    </div>
  </div>
));

export default Toast;
